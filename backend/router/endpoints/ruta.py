from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse,JSONResponse
from frontend.templates.templates import TEMPLATES
from pydantic import BaseModel
from backend.router.methods.obtenerRuta import obtener_distancia, calcular_ruta_mas_corta

router = APIRouter()


@router.post("/ruta", response_class=JSONResponse)
async def Ruta(direcciones: dict):
    origen = direcciones["origen"]
    destinos = {}

    for destino in direcciones["destinos"]:
        distancia = await obtener_distancia(origen, destino)
        destinos[destino] = distancia

    ruta = calcular_ruta_mas_corta(origen, destinos)

    return {
        "ruta": ruta
    }
