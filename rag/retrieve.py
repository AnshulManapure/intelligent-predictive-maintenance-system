from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_DIR")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def get_retriever():
    embeddings = GoogleGenerativeAIEmbeddings(
        model = os.getenv("GEMINI_EMBEDDING_MODEL"),
        api_key = os.getenv("GEMINI_API_KEY")
    )

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )

    return vector_store.as_retriever(
        search_kwargs = {"k":3}
    )

def retrieve_maintenance_context(top_features):
    retriever = get_retriever()

    feature_names = [item["feature"] for item in top_features]

    query = ("Maintenance guidance for turbofan engine sensors: " + ", ".join(feature_names))

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    return context