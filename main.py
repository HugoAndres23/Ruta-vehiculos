from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.router.endpoints import static, main, user, candidates, candidatures, votes

app = FastAPI(title="Ruta Vehicular")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(static.router, tags=["Static"])
# app.include_router(main.router, tags=["Login"])
app.include_router(user.router, tags=["User"])
# app.include_router(candidates.router, tags=["Candidates"])
# app.include_router(candidatures.router, tags=["Candidatures"])
# app.include_router(votes.router, tags=["Votes"])
