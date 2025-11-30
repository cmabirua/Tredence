# backend/app/routers/rooms.py
import inspect
import os
import uuid

from fastapi import APIRouter
from loguru import logger

from storage import create_room

router = APIRouter()


@router.post("/rooms", response_model=dict)
async def create_room_endpoint():
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    rid = uuid.uuid4().hex[:8]
    await create_room(rid, code="", language="python")
    return {"roomId": rid}
