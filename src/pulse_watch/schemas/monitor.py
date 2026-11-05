from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

class MonitorCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)

    url: HttpUrl

    method: Literal[
        "GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"
    ] = "GET"

    timeout: float = Field(default=10.0, gt=0,le=60)

    expected_status_codes: list[int] = Field(
        default_factory=lambda: [200],
        min_length=1
    )

    is_active: bool = True

class MonitorUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=150)

    url: HttpUrl | None = None

    method: Literal[
        "GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"
    ] | None = None
    
    timeout: float | None = Field(default=None, gt=0,le=60)
    
    expected_status_codes: list[int] | None = Field(
        default_factory=None,
        min_length=1
    )
    
    is_active: bool | None = None

class MonitorResponse(BaseModel):
    id: int
    name: str
    url: str
    method: str
    timeout: float
    expected_status_codes: list[int]
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)