from langchain.vectorstores import Chroma
from app.rag.embeddings import embeddings

def create_vectorstore(docs):
    return Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="data/chroma"
    )
