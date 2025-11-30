# backend/app/routers/autocomplete.py
from fastapi import APIRouter
from ..schemas import AutocompleteRequest, AutocompleteResponse

router = APIRouter()

@router.post("/autocomplete", response_model=AutocompleteResponse)
async def autocomplete(payload: AutocompleteRequest):
    code = payload.code or ""
    pos = payload.cursorPosition or len(code)
    snippet = code[max(0, pos-40):pos].strip()
    prefix = snippet.split()[-1] if snippet else ""

    if prefix.endswith("def") or prefix == "def":
        suggestion = " my_function(params):\n    \"\"\"docstring\"\"\"\n    pass"
    elif prefix in ("import", "from"):
        suggestion = " os"
    elif prefix.startswith("print"):
        suggestion = "('Hello')"
    else:
        suggestion = "# TODO: autocomplete suggestion"

    return {"suggestion": suggestion}
