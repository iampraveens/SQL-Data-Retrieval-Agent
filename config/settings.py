import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")
PROMPT_TEMPLATE_FILE = "templates/sql_prompt.txt"
SAMPLE_SIZE = int(os.getenv("SAMPLE_SIZE", 2))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()