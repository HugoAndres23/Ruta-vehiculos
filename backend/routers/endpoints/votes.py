from typing import Any
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from db import schemas
from db.supabase import register_vote, already_voted, get_candidatures
from db import deps

router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")


@router.post("/vote")
async def signin(
    request: Request,
    VoteCreate: schemas.VoteCreate,
    current_user: dict = Depends(deps.get_current_user),
) -> Any:
    candidatures = get_candidatures()
    if already_voted(VoteCreate.id_voter, VoteCreate.id_candidature):
        return templates.TemplateResponse(
            "voted.j2",
            {
                "request": request,
                "candidatures": candidatures,
                "already_voted": True,
                "voto": "",
            },
            409,
        )
    else:
        return templates.TemplateResponse(
            "voted.j2",
            {
                "request": request,
                "candidatures": candidatures,
                "already_voted": False,
                "voto": register_vote(VoteCreate),
            },
        )
