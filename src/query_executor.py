from typing import List, Tuple, Optional
from sqlalchemy import text
from sqlalchemy.engine import Engine
import streamlit as st
import logging

logger = logging.getLogger(__name__)

def execute_sql(engine: Engine, query: str) -> Tuple[Optional[List[Tuple]], Optional[List[str]]]:
    """Execute SQL query and fetch results."""
    # if not query.strip().upper().startswith("SELECT"):
    #     st.error("Only SELECT queries are allowed for safety.")
    #     return None, None
    
    with engine.connect() as conn:
        try:
            result = conn.execute(text(query))
            rows = result.fetchall()
            columns = list(result.keys())
            return rows, columns
        except Exception as e:
            logger.error(f"SQL execution error: {e}")
            st.error(f"Error executing SQL: {e}")
            return None, None