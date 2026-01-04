from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect
from app.cache.redis_client import redis_client

async def chat_socket(ws: WebSocket):
    await ws.accept()
    print("✅ WebSocket connected")

    from app.agents.rag_agent import rag_response  # lazy import

    try:
        while True:
            query = await ws.receive_text()

            cached = redis_client.get(query)
            if cached:
                # handle bytes OR str safely
                if isinstance(cached, bytes):
                    cached = cached.decode()
                await ws.send_text(cached)
                continue

            response = await rag_response(query)
            redis_client.setex(query, 300, response)

            await ws.send_text(response)

    except WebSocketDisconnect:
        # NORMAL disconnect (refresh, tab close)
        print("🔌 WebSocket disconnected normally")

    except Exception as e:
        # REAL server-side error
        print("❌ WebSocket internal error:", e)
