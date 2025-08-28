# SQL Data Retrieval Agent ⚡🗄️

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green?logo=database) ![LangChain](https://img.shields.io/badge/LangChain-Integration-orange) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)  

The **SQL Data Retrieval Agent** is a Python-based application designed to simplify interaction with SQL databases through natural language queries. Powered by Streamlit for the user interface, SQLAlchemy for database connectivity, and the Groq language model (via LangChain) for query generation, this tool enables users to generate SQL queries, execute them, and visualize the results in an intuitive and interactive manner. It is ideal for data analysts, developers, and database administrators who want to explore and visualize data without writing complex SQL queries manually.

---

## ✨ Key Features and Functionality

- **Natural Language Query Processing**: Translate natural language questions into accurate SQL queries using the Groq language model.
- **Dynamic Schema Retrieval**: Automatically fetches database schema and sample data to provide context for query generation.
- **Query Execution**: Executes generated SQL queries on a connected database using SQLAlchemy.
- **Data Visualization**: Supports multiple visualization types (bar, pie, line, scatter) using Matplotlib, based on user input or query context.
- **Interactive Streamlit Interface**: Provides a user-friendly web interface for inputting queries, viewing SQL code, results, and visualizations.
- **Error Handling and Logging**: Robust error handling and logging for reliable query execution and debugging.
- **Extensible Pipeline**: Modular design with separate components for schema loading, query generation, execution, and visualization.

---

## ⚙️ Installation and Setup Instructions

### 📋 Prerequisites

- **Python**: Version 3.8 or higher.
- **Database**: A running SQL database (e.g., PostgreSQL, MySQL) with relevant tables and data.
- **Groq API Key**: Obtain a key from [Groq Console](https://console.groq.com/keys).
- **Environment**: A `.env` file with required environment variables (see below).

### 🚀 Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iampraveens/sql-data-retrieval-agent.git
   cd sql-data-retrieval-agent
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root with the following content:
   ```plaintext
   DATABASE_URI=your_database_uri
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_PROJECT=your_langsmith_project_name
   SAMPLE_SIZE=2
   MAX_TOKENS=512
   LOG_LEVEL=INFO
   ```
   - Replace `your_database_uri` with your database connection string (e.g., `postgresql://user:password@localhost:5432/dbname`).
   - Replace `your_groq_api_key` with your Groq API key.
   - Replace `your_langchain_api_key` and `your_langsmith_project_name` with your LangChain credentials (optional for tracing).

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   The application will open in your default web browser at `http://localhost:8501`.

---

## 🎯 Usage Examples

### Example 1: Querying Total Spend by Customer
1. Open the Streamlit app in your browser.
2. In the chat input, enter:
   ```
   What is the total amount spent by each customer?
   ```
3. The app will:
   - Generate an SQL query like:
     ```sql
     SELECT c.customer_id, c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
     FROM customers c
     JOIN orders o ON c.customer_id = o.customer_id
     GROUP BY c.customer_id, c.first_name, c.last_name
     ORDER BY total_spent DESC;
     ```
   - Display the query, execute it, and show the results in a table.
   - Optionally generate a visualization if specified (e.g., bar plot).

### Example 2: Visualizing Order Totals
1. Enter a query with a visualization request:
   ```
   How do order totals correlate with the number of items in the order? and give in bar plot
   ```
2. The app will:
   - Generate and execute an SQL query.
   - Display the results in a table.
   - Render a bar plot comparing total items and order amounts.

### Notes
- Ensure your database has relevant tables (e.g., `customers`, `orders`, `order_items`, `products`) with appropriate columns.
- Use keywords like `bar`, `pie`, `line`, or `scatter` in your query to trigger specific visualizations.

---

## 📂 File Structure Overview

```
sql-data-retrieval-agent/
├── README.md               # Project documentation
├── app.py                  # Main Streamlit application
├── LICENSE                 # MIT License file
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup script
├── template.sh             # Script to create project structure
├── config/                 # Configuration files
│   ├── __init__.py
│   └── settings.py         # Environment variable loading
├── prompts/                # Prompt templates
│   └── sql_prompt.txt      # Template for SQL query generation
├── research/               # Jupyter notebooks for experiments
│   ├── experiments.ipynb   # Main experimentation notebook
│   └── trials.ipynb        # Additional trials and testing
└── src/                    # Source code
    ├── __init__.py
    ├── pipeline.py         # Orchestrates query processing
    ├── query_executor.py   # Executes SQL queries
    ├── schema_loader.py    # Loads database schema and prompts
    ├── sql_generator.py    # Generates SQL queries using Groq
    ├── utils.py            # Utility functions (e.g., SQL extraction)
    └── visualizer.py       # Handles data visualization
```

---

## 📦 Dependencies and Requirements

The project requires the following Python packages (listed in `requirements.txt`):
- `streamlit`: For the web interface.
- `psycopg2`: For PostgreSQL database connectivity (if using PostgreSQL).
- `sqlalchemy`: For database operations.
- `python-dotenv`: For loading environment variables.
- `pandas`: For data manipulation and display.
- `matplotlib`: For data visualization.
- `langchain-groq`: For interacting with the Groq language model.

Install them using:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. **Fork the Repository**:
   Fork the project on GitHub and clone your fork locally.

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**:
   - Follow the project’s coding style and structure.
   - Add or update tests if applicable.
   - Update documentation (e.g., `README.md`, docstrings) for new features.

4. **Test Your Changes**:
   - Ensure the application runs without errors.
   - Test with a sample database to verify query generation and visualization.

5. **Submit a Pull Request**:
   - Push your branch to your fork.
   - Open a pull request with a clear description of your changes and their purpose.
   - Reference any related issues.

6. **Code Review**:
   - Respond to feedback during the review process.
   - Ensure your code adheres to the project’s standards.

Please ensure your contributions align with the project’s MIT License.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed with ❤️ by **Praveen S** ([GitHub](https://github.com/iampraveens))