# backend/app/schemas.py

from pydantic import BaseModel


class AutocompleteRequestInput(BaseModel):
    code: str
    cursorPosition: int
    language: str = "python"


class AutocompleteRequest(AutocompleteRequestInput):
    pass


class AutocompleteResponseInput(BaseModel):
    suggestion: str


class AutocompleteResponse(AutocompleteResponseInput):
    pass
