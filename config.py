import os
from pathlib import Path

# --- 1. Define Base Directory ---
BASE_DIR = Path(__file__).resolve().parent

# --- 2. Define Data Directory ---
# We will put PDFs inside a folder named 'data'
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# --- 3. Define Vector DB Directory ---
DB_DIR = BASE_DIR / "vector_db"

# --- 4. Define Specific File Path ---
# IMPORTANT: Put your PDF file inside the 'data' folder
PDF_FILENAME = "FULLBOOKPHYSICS.pdf"
PDF_PATH = DATA_DIR / PDF_FILENAME

# --- 5. Model Configuration ---
LLM_MODEL = "llama3"
EMBEDDING_MODEL = "nomic-embed-text"