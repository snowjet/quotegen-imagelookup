from fastapi import APIRouter

from api.api_v2.endpoints import image
from core.log import logger

api_router = APIRouter()
api_router.include_router(image.router, prefix="/image", tags=["image"])
