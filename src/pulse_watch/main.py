from fastapi import FastAPI
from pulse_watch.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API Monitoring Platform"
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