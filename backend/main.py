from fastapi import FastAPI
from routers.endpoints import static, main, user, candidates, candidatures, votes

app = FastAPI(
    title='E-Voting'
)

app.include_router(static.router, tags=["Static"])
app.include_router(main.router, tags=["Login"])
app.include_router(user.router, tags=["User"])
app.include_router(candidates.router, tags=["Candidates"])
app.include_router(candidatures.router, tags=["Candidatures"])
app.include_router(votes.router, tags=["Votes"])