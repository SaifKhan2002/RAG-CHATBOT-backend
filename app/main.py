from fastapi import FastAPI, WebSocket
from app.websocket import chat_socket
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.websocket("/ws/chat")
async def websocket_endpoint(ws: WebSocket):
    await chat_socket(ws)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)