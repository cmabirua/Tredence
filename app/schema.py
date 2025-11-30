# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional

class RoomCreateResponse(BaseModel):
    roomId: str

class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str = "python"

class AutocompleteResponse(BaseModel):
    suggestion: str

class EditMessage(BaseModel):
    type: str
    code: Optional[str] = None
    cursor: Optional[dict] = None
