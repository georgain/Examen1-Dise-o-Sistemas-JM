from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.models import Priority, TaskStatus


class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority
    assignee_id: Optional[str] = None


class TaskResponse(BaseModel):
    id: str
    title: str
    priority: Priority
    status: TaskStatus
    created_at: datetime