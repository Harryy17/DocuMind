import shutil
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import config

def create_vector_db():
    # 1. Check if PDF exists
    if not config.PDF_PATH.exists():
        print(f"❌ Error: File not found at {config.PDF_PATH}")
        print(f"   Please move '{config.PDF_FILENAME}' into the 'data' folder.")
        return

    # 2. Clear old database to avoid duplicates
    if config.DB_DIR.exists():
        shutil.rmtree(config.DB_DIR)

    # 3. Load PDF
    print(f"📄 Loading {config.PDF_FILENAME}...")
    loader = PyPDFLoader(str(config.PDF_PATH))
    docs = loader.load()

    # 4. Split Text
    print("✂️  Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    total_chunks = len(splits)
    print(f"   Split into {total_chunks} chunks.")

    # 5. Create Embeddings & Store (BATCHED)
    print("💾 Creating Vector Store (in batches)...")
    embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)
    
    # Initialize the database (empty)
    vectorstore = Chroma(
        persist_directory=str(config.DB_DIR), 
        embedding_function=embeddings
    )

    # Define batch size (must be < 166)
    batch_size = 100 
    
    # Loop through splits and add them in batches
    for i in range(0, total_chunks, batch_size):
        batch = splits[i : i + batch_size]
        print(f"   Processing batch {i} to {min(i + batch_size, total_chunks)}...")
        vectorstore.add_documents(documents=batch)
        # Small sleep to prevent rate limits (optional but good practice)
        time.sleep(0.1)

    print("✅ Success! Vector database created.")

if __name__ == "__main__":
    create_vector_db()