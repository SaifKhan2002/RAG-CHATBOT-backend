from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="qwen2.5:0.5b-instruct-q8_0"  # much smaller, fits in memory
)
