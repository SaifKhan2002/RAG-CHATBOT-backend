def route_query(query: str):
    if "service" in query.lower():
        return "rag"
    return "general"
