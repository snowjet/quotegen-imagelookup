from fastapi import FastAPI

from api.api_v1.api import api_router
from core.config import settings
from core.log import logger
from fastapi.staticfiles import StaticFiles

logger.info("Starting App")

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix=settings.API_V1_STR)
