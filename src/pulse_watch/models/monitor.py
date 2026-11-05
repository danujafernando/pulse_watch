from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    Integer,
    JSON,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from pulse_watch.db.base import Base

class Monitor(Base):
    __tablename__ = "monitors"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False
    )

    method: Mapped[str] = mapped_column(
        String(10),
        default="GET",
        nullable=False
    )

    timeout: Mapped[float] = mapped_column(
        Float,
        default=10.0,
        nullable=False
    )

    expected_status_codes: Mapped[list[int]] = mapped_column(
        JSON,
        default=lambda: [200],
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )