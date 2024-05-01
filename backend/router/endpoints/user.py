from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from frontend.templates.templates import TEMPLATES

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
@router.get("/login", response_class=HTMLResponse)
async def Home(request: Request):
    title = "E-voting | Login"
    return TEMPLATES.TemplateResponse(
        "login.j2",
        {
            "request": request,
            "title": title,
        },
    )
