from langchain_community.vectorstores import Chroma
from app.rag.embeddings import embeddings

db = Chroma(
    persist_directory="data/chroma",
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)
