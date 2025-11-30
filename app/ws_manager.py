# backend/app/ws_manager.py
import inspect
import os
from typing import Dict, List

from fastapi import WebSocket
from loguru import logger


class ConnectionManager:
    def __init__(self):
        logger.info(
            f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
        )
        # room_id -> list[WebSocket]
        self.active: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        logger.info(
            f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
        )
        await websocket.accept()
        self.active.setdefault(room_id, []).append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        logger.info(
            f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
        )
        conns = self.active.get(room_id, [])
        if websocket in conns:
            conns.remove(websocket)
        if not conns:
            self.active.pop(room_id, None)

    async def broadcast(self, room_id: str, message: dict, sender: WebSocket = None):
        logger.info(
            f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
        )
        conns = list(self.active.get(room_id, []))
        for ws in conns:
            if ws is sender:
                continue
            try:
                await ws.send_json(message)
            except Exception:
                pass


manager = ConnectionManager()
