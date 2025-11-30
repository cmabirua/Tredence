# backend/app/ws_manager.py
from typing import Dict, List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        # room_id -> list[WebSocket]
        self.active: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active.setdefault(room_id, []).append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        conns = self.active.get(room_id, [])
        if websocket in conns:
            conns.remove(websocket)
        if not conns:
            self.active.pop(room_id, None)

    async def broadcast(self, room_id: str, message: dict, sender: WebSocket = None):
        conns = list(self.active.get(room_id, []))
        for ws in conns:
            if ws is sender:
                continue
            try:
                await ws.send_json(message)
            except Exception:
                # ignore errors for prototype
                pass

manager = ConnectionManager()
