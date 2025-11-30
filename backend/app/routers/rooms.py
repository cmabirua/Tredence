# backend/app/routers/rooms.py
from fastapi import APIRouter
from ..storage import create_room
import uuid

router = APIRouter()

@router.post("/rooms", response_model=dict)
async def create_room_endpoint():
    rid = uuid.uuid4().hex[:8]
    await create_room(rid, code="", language="python")
    return {"roomId": rid}
