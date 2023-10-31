from typing import Any
from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db.supabase import get_candidates, get_candidate_by_id
from db import deps


router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")
router.mount("/static", StaticFiles(directory=".\.\static"), name="static")


@router.get("/candidates/{id}")
async def candidate_by_id(
    id: int, current_user: dict = Depends(deps.get_current_user)
) -> Any:
    return get_candidate_by_id(id)


@router.get("/candidates")
async def candidates(current_user: dict = Depends(deps.get_current_user)) -> Any:
    return get_candidates()
