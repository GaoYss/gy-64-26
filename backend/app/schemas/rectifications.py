from datetime import date
from typing import Literal

from pydantic import BaseModel


RectificationStatus = Literal["pending", "in_progress", "completed", "reinspected"]
RectificationPriority = Literal["low", "medium", "high"]


class RectificationBase(BaseModel):
    project_id: int
    project_name: str
    inspection_id: int | None = None
    title: str
    description: str
    responsible: str
    deadline: date
    priority: RectificationPriority = "medium"
    status: RectificationStatus = "pending"
    progress: str = ""


class RectificationCreate(RectificationBase):
    pass


class RectificationUpdate(BaseModel):
    project_id: int | None = None
    project_name: str | None = None
    inspection_id: int | None = None
    title: str | None = None
    description: str | None = None
    responsible: str | None = None
    deadline: date | None = None
    priority: RectificationPriority | None = None
    status: RectificationStatus | None = None
    progress: str | None = None


class Rectification(RectificationBase):
    id: int
    created_at: date
