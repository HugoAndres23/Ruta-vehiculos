from typing import Any
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db.supabase import get_candidates, get_candidatures

router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")
router.mount("/static", StaticFiles(directory=".\.\static"), name="static")


@router.get("/main")
async def main(request: Request, candidatura: int = 1) -> Any:
    title = "E-voting | main"
    candidates = get_candidates(candidatura)
    candidatures = get_candidatures()
    return templates.TemplateResponse(
        "main.j2",
        {
            "request": request,
            "title": title,
            "candidates": candidates,
            "candidatures": candidatures,
        },
    )
