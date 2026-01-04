SYSTEM_PROMPT = """
You are an AI assistant for XSPACE TECHNOLOGIES PVT LTD.
You ONLY answer based on the provided context.
Be professional, concise, and accurate.
If info is missing, say you don't know.
"""

def build_prompt(context, query):
    return f"""
{SYSTEM_PROMPT}

Context:
{context}

User Question:
{query}

Answer:
"""
