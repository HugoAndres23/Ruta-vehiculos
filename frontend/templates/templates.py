from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH))
