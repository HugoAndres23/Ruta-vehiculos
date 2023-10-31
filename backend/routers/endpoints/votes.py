from typing import Any
from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from db import schemas
from db.supabase import register_vote, already_voted
from db import deps

router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")


@router.post("/vote")
async def signin(
    VoteCreate: schemas.VoteCreate, current_user: dict = Depends(deps.get_current_user)
) -> Any:
    if already_voted(VoteCreate.id_voter, VoteCreate.id_candidature):
        return templates.TemplateResponse(
            "main.j2",
            {
                "request": request,
                "title": title,
                "candidates": candidates,
                "candidatures": candidatures,
            },
        )
    return register_vote(VoteCreate)
