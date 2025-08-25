from typing import List, Tuple, Optional
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from src.schema_loader import load_db_schema, load_prompt_template
from src.sql_generator import generate_sql_query
from src.query_executor import execute_sql
from src.visualizer import detect_plot_type, plot_results
from config.settings import DATABASE_URI, GROQ_API_KEY, PROMPT_TEMPLATE_FILE, SAMPLE_SIZE, MAX_TOKENS

class QueryPipeline:
    """Orchestrates the query processing pipeline."""
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.schema = load_db_schema(self.engine, sample_size=SAMPLE_SIZE)
        self.template = load_prompt_template(PROMPT_TEMPLATE_FILE)
    
    def process_query(self, question: str) -> Tuple[str, Optional[List[Tuple]], Optional[List[str]], Optional[str], Optional[plt.Figure]]:
        """Process a natural language query and return SQL, results, and visualization."""
        sql_query = generate_sql_query(
            GROQ_API_KEY,
            self.template,
            self.schema,
            question,
            self.engine.dialect.name,
            max_tokens=MAX_TOKENS
        )
        
        if not sql_query:
            return "", None, None, None, None
        
        results, columns = execute_sql(self.engine, sql_query)
        if results is None or columns is None:
            return sql_query, None, None, None, None
        
        plot_type = detect_plot_type(question)
        fig = None
        if plot_type:
            fig = plot_results(columns, results, plot_type)
        
        return sql_query, results, columns, plot_type, fig