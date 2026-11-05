from contextlib import asynccontextmanager

from fastapi import FastAPI

from pulse_watch.api.router import api_router
from pulse_watch.core.config import settings
from pulse_watch.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API Monitoring Platform",
    lifespan=lifespan
)

app.include_router(
    api_router,
    prefix="/api"
)

@app.get("/")
def home():
    return {
        "application": settings.app_name,
        "message": "Welcome to PulseWatch"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }