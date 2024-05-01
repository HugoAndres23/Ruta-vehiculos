from fastapi import APIRouter, Request
from fastapi.responses import FileResponse


router = APIRouter()


@router.get("/static/{directoryname}/{filename}")
def get_static_file(request: Request, directoryname: str, filename: str):
    return FileResponse(f"static/{directoryname}/{filename}")
