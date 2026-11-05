from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from pulse_watch.models.monitor import Monitor
from pulse_watch.repositories.monitor_repository import MonitorRepository

class MonitorService:

    def __init__(self, db: Session):
        self.repository = MonitorRepository(db)

    def create_monitor(self, data: dict) -> Monitor:
        data["url"] = str(data["url"])

        return self.repository.create(data)

    def get_monitors(self) -> list[Monitor]:
        return self.repository.get_all()

    def get_monitor(self, monitor_id: int) -> Monitor:
        monitor = self.repository.get_by_id(monitor_id)

        if not monitor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Monitor not found"
            )

        return monitor

    def update_monitor(
        self,
        monitor_id: int,
        data: dict
    ) -> Monitor:

        monitor = self.get_monitor(monitor_id)

        if "url" in data:
            data["url"] = str(data["url"])

        return self.repository.update(monitor, data)

    def delete_monitor(self, monitor_id: int) -> None:
        monitor = self.get_monitor(monitor_id)

        self.repository.delete(monitor)