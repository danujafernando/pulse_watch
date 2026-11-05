from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from pulse_watch.db.session import get_db
from pulse_watch.schemas.monitor import (
    MonitorCreate,
    MonitorResponse,
    MonitorUpdate
)
from pulse_watch.services.monitor_service import MonitorService

router = APIRouter()

def get_monitor_service(
    db: Session = Depends(get_db)
) -> MonitorService:
    return MonitorService(db)

@router.post(
    "",
    response_model=MonitorResponse,
    status_code=status.HTTP_201_CREATED
)
def create_monitor(
    data: MonitorCreate,
    service: MonitorService = Depends(get_monitor_service)
):
    return service.create_monitor(data.model_dump())

@router.get(
    "",
    response_model=list[MonitorResponse]
)
def get_monitors(
    service: MonitorService = Depends(get_monitor_service)
):
    return service.get_monitors()

@router.get(
    "/{monitor_id}",
    response_model=MonitorResponse
)
def get_monitor(
    monitor_id: int,
    service: MonitorService = Depends(get_monitor_service)
):
    return service.get_monitor(monitor_id)

@router.put(
    "/{monitor_id}",
    response_model=MonitorResponse
)
def update_monitor(
    monitor_id: int,
    data: MonitorUpdate,
    service: MonitorService = Depends(get_monitor_service)
):
    update_data = data.model_dump(exclude_unset=True)

    return service.update_monitor(monitor_id, update_data)


@router.delete(
    "/{monitor_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_monitor(
    monitor_id: int,
    service: MonitorService = Depends(get_monitor_service)
):
    service.delete_monitor(monitor_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)