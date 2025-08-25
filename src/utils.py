import re
import logging

logger = logging.getLogger(__name__)

def extract_sql(text: str) -> str:
    """Extract SQL query from model response."""
    try:
        match = re.search(r"```sql\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else text.strip()
    except Exception as e:
        logger.error(f"Error extracting SQL: {e}")
        return text.strip()