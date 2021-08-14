from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

view = APIRouter()
templates = Jinja2Templates(directory="templates")


@view.get("/", response_class=JSONResponse)
async def home() -> JSONResponse:
    """Home Page

    Returns:
        JSONResponse: Hello World!
    """
    message = {"stauts": "success", "message": "Hello World!"}
    return JSONResponse(content=message)
