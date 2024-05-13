from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.router.endpoints import static, main, ruta

app = FastAPI(title="Ruta Vehicular")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(static.router, tags=["Static"])
app.include_router(main.router, tags=["User"])
app.include_router(ruta.router, tags=["Ruta"])
