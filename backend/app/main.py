# backend/app/main.py
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .routers import rooms, autocomplete
from .ws_manager import manager
from .storage import get_room, create_room, upsert_room_code

app = FastAPI(title="PairProg Prototype (JSON storage)")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(rooms.router)
app.include_router(autocomplete.router)

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)

    # ensure room exists
    r = await get_room(room_id)
    if not r:
        await create_room(room_id, code="", language="python")
        r = await get_room(room_id)

    # send current code on connect
    try:
        await websocket.send_json({"type": "sync", "code": r.get("code", "")})
    except Exception:
        pass

    try:
        while True:
            data = await websocket.receive_json()
            typ = data.get("type")
            if typ == "edit":
                code = data.get("code", "")
                # persist to JSON file (last-write-wins)
                await upsert_room_code(room_id, code)
                # broadcast to other clients
                await manager.broadcast(room_id, {"type": "edit", "code": code}, sender=websocket)
            elif typ == "cursor":
                await manager.broadcast(room_id, {"type": "cursor", "cursor": data.get("cursor")}, sender=websocket)
            else:
                # ignore unknown messages
                pass
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
    except Exception:
        manager.disconnect(room_id, websocket)
        try:
            await websocket.close()
        except Exception:
            pass

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
