from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from frontend.templates.templates import TEMPLATES
from pydantic import BaseModel

router = APIRouter()


class RutaRequest(BaseModel):
    origen: str
    destino: str


@router.post("/ruta", response_class=HTMLResponse)
async def Ruta(request: Request, direcciones: RutaRequest):
    origen = direcciones.origen
    destino = direcciones.destino

    return (
        {
            "request": request,
        },
    )
