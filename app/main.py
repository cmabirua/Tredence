import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import os,inspect

from routers import autocomplete, rooms
from storage import create_room, get_room, upsert_room_code
from ws_manager import manager

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(rooms.router)
app.include_router(autocomplete.router)


@app.websocket("/ws/{room_id}")
async def handle_room_id(websocket: WebSocket, room_id: str):
    logger.info(f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}")
    await manager.connect(room_id, websocket)
    r_id = await get_room(room_id)
    if not r_id:
        await create_room(room_id, code="", language="python")
        r_id = await get_room(room_id)
    try:
        await websocket.send_json({"type": "sync", "code": r_id.get("code", "")})
    except Exception:
        pass

    try:
        while True:
            data = await websocket.receive_json()
            typ = data.get("type")
            if typ == "edit":
                code = data.get("code", "")
                await upsert_room_code(room_id, code)
                await manager.broadcast(
                    room_id, {"type": "edit", "code": code}, sender=websocket
                )
            elif typ == "cursor":
                await manager.broadcast(
                    room_id,
                    {"type": "cursor", "cursor": data.get("cursor")},
                    sender=websocket,
                )
            else:
                pass
    except Exception:
        manager.disconnect(room_id, websocket)
        try:
            await websocket.close()
        except Exception:
            pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
