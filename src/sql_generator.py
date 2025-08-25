from groq import Groq
import logging
import streamlit as st
from src.utils import extract_sql

logger = logging.getLogger(__name__)

def generate_sql_query(
    client: Groq,
    template: str,
    schema: str,
    question: str,
    dialect: str,
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.0,
    max_tokens: int = 512
) -> str:
    """Generate SQL query using the Groq model."""
    if not template or not schema:
        return ""
    
    prompt = template.format(schema=schema, question=question, dialect=dialect)
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1.0,
            stream=False
        )
        raw_response = completion.choices[0].message.content.strip()
        logger.debug(f"Raw model response: {raw_response}")
        return extract_sql(raw_response)
    except Exception as e:
        logger.error(f"Error generating SQL: {e}")
        st.error(f"Error generating SQL query: {e}")
        return ""