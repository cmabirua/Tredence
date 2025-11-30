# backend/app/storage.py
import asyncio
import inspect
import json
import os
import time
from typing import Dict, Optional

from loguru import logger

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOMS_PATH = os.path.join(ROOT, "..", "rooms.json")
async_lock = asyncio.Lock()


def file_check():
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    path = os.path.abspath(ROOMS_PATH)
    if not os.path.exists(path):
        # create file with empty dict
        with open(path, "w", encoding="utf-8") as f:
            json.dump({}, f)


async def read_all_rooms() -> Dict[str, dict]:
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    file_check()

    # run file IO in thread to avoid blocking event loop
    def read_all_rooms_utils():
        logger.info(
            f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
        )
        with open(ROOMS_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    return await asyncio.to_thread(read_all_rooms_utils)


async def write_all_rooms(data: Dict[str, dict]) -> None:
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    file_check()
    async with async_lock:

        def write_all_rooms_utils():
            logger.info(
                f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
            )
            tmp = ROOMS_PATH + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp, ROOMS_PATH)

        await asyncio.to_thread(write_all_rooms_utils)


async def get_room(room_id: str) -> Optional[dict]:
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    rooms = await read_all_rooms()
    return rooms.get(room_id)


async def create_room(room_id: str, code: str = "", language: str = "python") -> dict:
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    rooms = await read_all_rooms()
    if room_id in rooms:
        return rooms[room_id]
    entry = {
        "room_id": room_id,
        "code": code,
        "language": language,
        "created_at": int(time.time()),
    }
    rooms[room_id] = entry
    await write_all_rooms(rooms)
    return entry


async def upsert_room_code(room_id: str, code: str) -> None:
    logger.info(
        f"{os.path.basename(__file__)}::{inspect.currentframe().f_code.co_name}"
    )
    rooms = await read_all_rooms()
    if room_id not in rooms:
        rooms[room_id] = {
            "room_id": room_id,
            "code": code,
            "language": "python",
            "created_at": int(time.time()),
        }
    else:
        rooms[room_id]["code"] = code
    await write_all_rooms(rooms)
