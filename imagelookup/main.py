from fastapi import FastAPI

from core.config import settings
from core.log import logger
from fastapi.staticfiles import StaticFiles

if 'v2' in str(settings.API_V1_STR):
    from api.api_v2.api import api_router
    start_msg = "Starting App - Using API v2"
else:
    from api.api_v1.api import api_router
    start_msg = "Starting App - Using API v1"
logger.info(start_msg)


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix=settings.API_V1_STR)

