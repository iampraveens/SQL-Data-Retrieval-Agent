import streamlit as st
import pandas as pd
import os
from src.pipeline import QueryPipeline
from config.settings import (
    DATABASE_URI, GROQ_API_KEY, LANGCHAIN_API_KEY, LANGSMITH_PROJECT, LANGCHAIN_ENDPOINT
)

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"] = LANGSMITH_PROJECT
os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_ENDPOINT


def main():

    """Main Streamlit app function."""
    st.set_page_config(page_title="SQL Query Visualizer", page_icon="📊", layout="centered")
    
    # Sidebar for configuration
    st.sidebar.header("Configuration")
    st.sidebar.write("Ensure .env file contains DATABASE_URI and GROQ_API_KEY.")
    
    # Main content
    st.title("SQL Query Visualizer")
    st.markdown("Chat with the app to generate SQL queries and visualize results!")
    
    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("sql_query"):
                st.code(message["sql_query"], language="sql")
            if message.get("dataframe") is not None:
                st.dataframe(message["dataframe"], use_container_width=True)
            if message.get("plot"):
                st.pyplot(message["plot"])
    
    # Chat input
    question = st.chat_input("Enter your query (e.g., What are the top 5 products by total revenue generated from orders?")
    
    if question:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        
        if not DATABASE_URI or not GROQ_API_KEY:
            error_msg = "Missing environment variables: DATABASE_URI or GROQ_API_KEY"
            st.session_state.chat_history.append({"role": "assistant", "content": error_msg})
            with st.chat_message("assistant"):
                st.error(error_msg)
            return
        
        with st.spinner("Processing your query..."):
            try:
                pipeline = QueryPipeline()
                sql_query, results, columns, plot_type, fig = pipeline.process_query(question)
                
                if not sql_query:
                    return
                
                # Display SQL query
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "Generated SQL Query:",
                    "sql_query": sql_query
                })
                with st.chat_message("assistant"):
                    st.markdown("Generated SQL Query:")
                    st.code(sql_query, language="sql")
                
                if results is None or columns is None:
                    return
                
                # Display results
                df = pd.DataFrame(results, columns=columns)
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "Query Results:",
                    "dataframe": df
                })
                with st.chat_message("assistant"):
                    st.markdown("Query Results:")
                    st.dataframe(df, use_container_width=True)
                
                # Plotting
                if plot_type and fig:
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": "Visualization:",
                        "plot": fig
                    })
                    with st.chat_message("assistant"):
                        st.markdown("Visualization:")
                        st.pyplot(fig)
                
            except Exception as e:
                error_msg = f"An unexpected error occurred: {e}"
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg})
                with st.chat_message("assistant"):
                    st.error(error_msg)

if __name__ == "__main__":
    main()