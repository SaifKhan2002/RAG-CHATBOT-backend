from langchain_community.llms import Ollama
from app.rag.retriever import retriever
from app.prompts.prompts import build_prompt
import asyncio

llm = Ollama(model="qwen2.5:0.5b-instruct-q8_0")

async def rag_response(query: str) -> str:
    loop = asyncio.get_running_loop()

    docs = await loop.run_in_executor(
        None, lambda: retriever._get_relevant_documents(query, run_manager=None)
    )

    context = "\n".join(d.page_content for d in docs)
    prompt = build_prompt(context, query)

    response = await loop.run_in_executor(
        None, lambda: llm.generate([prompt])
    )

    return response.generations[0][0].text
