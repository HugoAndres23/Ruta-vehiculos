import cssmin
import jsmin
from fastapi import APIRouter, Request
from fastapi.responses import Response, FileResponse
from frontend.templates.templates import BASE_PATH, TEMPLATES

router = APIRouter()

static_dir = BASE_PATH.parent / "static"
css_folder = static_dir / "css"
js_folder = static_dir / "js"


@router.get("/assets/{directoryname}")
def get_static_file(request: Request, directoryname: str):
    if directoryname == "js":
        js_files = js_folder.glob("*.js")

        minified_js = ""
        for js_file in js_files:
            with open(js_file, "r") as file:
                js_content = file.read()
                minified_js += jsmin.jsmin(js_content)

        return Response(content=minified_js, media_type="text/javascript")

    elif directoryname == "css":
        css_files = css_folder.glob("*.css")

        minified_css = ""
        for css_file in css_files:
            with open(css_file, "r") as file:
                css_content = file.read()
                minified_css += cssmin.cssmin(css_content)

        return Response(content=minified_css, media_type="text/css")
    else:
        return Response(content="Directory not supported", status_code=404)
