from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from frontend.templates.templates import TEMPLATES

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
@router.get("/home", response_class=HTMLResponse)
async def Home(request: Request):
    title = "E-voting | Inicio"
    return TEMPLATES.TemplateResponse(
        "main.j2",
        {
            "request": request,
            "title": title,
        },
    )
