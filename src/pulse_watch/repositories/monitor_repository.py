from sqlalchemy import select
from sqlalchemy.orm import Session

from pulse_watch.models.monitor import Monitor

class MonitorRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Monitor:
        monitor = Monitor(**data)

        self.db.add(monitor)
        self.db.commit()
        self.db.refresh(monitor)

        return monitor

    def get_all(self) -> list[Monitor]:
        statement = select(Monitor).order_by(Monitor.id.desc())

        return list(self.db.scalars(statement).all())

    def get_by_id(self, monitor_id: int) -> Monitor | None:
        return self.db.get(Monitor, monitor_id)

    def update(self, monitor: Monitor, data: dict) -> Monitor:
        for key, value in data.items():
            setattr(monitor, key, value)

        self.db.commit()
        self.db.refresh(monitor)

        return monitor

    def delete(self, monitor: Monitor) -> None:
        self.db.delete(monitor)
        self.db.commit()