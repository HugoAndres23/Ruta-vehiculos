# from typing import Any
# from fastapi import APIRouter, Request
# from fastapi.templating import Jinja2Templates

# router = APIRouter()
# templates = Jinja2Templates(directory="routers/templates")


# @router.get("/main")
# async def main(request: Request, candidatura: int = 1) -> Any:
#     title = "E-voting | main"
#     candidates = get_candidates(candidatura)
#     candidatures = get_candidatures()
#     return templates.TemplateResponse(
#         "main.j2",
#         {
#             "request": request,
#             "title": title,
#             "candidates": candidates,
#             "candidatures": candidatures,
#         },
#     )
