import logging
from sqlalchemy import MetaData, text
from sqlalchemy.engine import Engine
import streamlit as st

logger = logging.getLogger(__name__)

def load_db_schema(engine: Engine, sample_size: int = 2) -> str:
    """Retrieve the database schema with sample data for each table."""
    try:
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        schema_parts = []
        with engine.connect() as conn:
            for table in metadata.tables.values():
                schema_parts.append(f"\nTable: {table.name}")
                columns = ", ".join([f"{col.name} ({col.type})" for col in table.columns])
                schema_parts.append(f"Columns: {columns}")
                
                try:
                    result = conn.execute(
                        text(f"SELECT * FROM {table.name} LIMIT :limit"),
                        {"limit": sample_size}
                    )
                    rows = result.fetchall()
                    if rows:
                        schema_parts.append("Sample rows:")
                        for row in rows:
                            schema_parts.append(f"  {dict(row._mapping)}")
                    else:
                        schema_parts.append("Sample rows: <no data>")
                except Exception as e:
                    logger.error(f"Error fetching samples for table {table.name}: {e}")
                    schema_parts.append(f"Sample rows: <error retrieving data: {str(e)}>")
        
        return "\n".join(schema_parts).strip()
    except Exception as e:
        logger.error(f"Error retrieving schema: {e}")
        st.error(f"Failed to retrieve database schema: {e}")
        return ""

def load_prompt_template(file_path: str) -> str:
    """Load the prompt template from file."""
    try:
        with open(file_path, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        logger.critical(f"Prompt template file not found: {file_path}")
        st.error(f"Prompt template file not found: {file_path}")
        return ""
    except Exception as e:
        logger.error(f"Error loading prompt template: {e}")
        st.error(f"Error loading prompt template: {e}")
        return ""