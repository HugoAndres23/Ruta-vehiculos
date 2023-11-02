from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from db import schemas
from db import deps
from core import security
from core.config import settings
from db.supabase import login, register_voter

router = APIRouter()
templates = Jinja2Templates(directory="routers/templates")
router.mount("/static", StaticFiles(directory=".\.\static"), name="static")


@router.get("/", response_class=HTMLResponse)
@router.get("/login", response_class=HTMLResponse)
async def Home(request: Request):
    title = "E-voting | Login"
    return templates.TemplateResponse(
        "login.j2",
        {
            "request": request,
            "title": title,
        },
    )


@router.post("/login", response_model=schemas.Token)
async def login_access_token(login_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = login(login_data.username, login_data.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user["id"], expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/register")
async def signin(VoterCreate: schemas.VoterCreate) -> Any:
    return register_voter(VoterCreate)


@router.get("/me")
def read_user_me(current_user: dict = Depends(deps.get_current_user)) -> Any:
    """
    Get current user.
    """
    return current_user
