from langchain.document_loaders import WebBaseLoader

URLS = [
    "https://www.xpacetechnologies.com/"
]

def load_docs():
    loader = WebBaseLoader(URLS)
    return loader.load()
