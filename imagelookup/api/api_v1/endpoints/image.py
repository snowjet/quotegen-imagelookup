from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from fastapi import Depends, Request

from crud import image as crudImage
from core.config import settings
from core.log import logger

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("", response_class=JSONResponse)
async def get_image_by_name(request: Request, name: str = None):
    logger.info("name Image Requested: " + str(name))
    try:
        image = crudImage.get_image_as_base64(name=name)
        return {"image": image}
    except ValueError:
        raise HTTPException(status_code=404, detail="name not found")


@router.get("/", response_class=JSONResponse)
async def get_image_by_name(request: Request, name: str = None):
    try:
        image = crudImage.get_image_as_base64(name=name)
        return {"image": image}
    except ValueError:
        raise HTTPException(status_code=404, detail="name not found")


@router.get("/html/{name}", response_class=HTMLResponse)
async def get_image_by_name_html(request: Request, name: str = None):
    logger.info("name Image Requested: " + name)
    try:
        image = crudImage.get_image_as_base64(name=name)
        return templates.TemplateResponse(
        "index.html", {"request": request, "image": image}
    )
    except ValueError:
        raise HTTPException(status_code=404, detail="name not found")