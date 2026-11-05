from fastapi import APIRouter

from pulse_watch.api.v1 import monitors

api_router = APIRouter()

api_router.include_router(
    monitors.router,
    prefix="/monitors",
    tags=["Monitors"]
)