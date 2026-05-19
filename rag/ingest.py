from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

DOC_PATH = os.getenv("DOC_PATH")
CHROMA_DIR = os.getenv("CHROMA_DIR")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def ingest_documents():
    loader = TextLoader(DOC_PATH, encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size = 700, chunk_overlap = 100)
    chunks = splitter.split_documents(documents=documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model=os.getenv("GEMINI_EMBEDDING_MODEL"),
        api_key=os.getenv("GEMINI_API_KEY")
        )
    
    print(f"Loaded {len(documents)} documents")
    print(f"Generated {len(chunks)} chunks")
    
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME
    )

    print(f"Ingested {len(chunks)} chunks into ChromaDB.")


if __name__ == "__main__":
    ingest_documents()