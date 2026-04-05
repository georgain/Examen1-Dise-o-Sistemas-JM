from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

from domain.task_status import TaskStatus
from domain.priority import Priority


@dataclass
class Task:
    id: str
    title: str
    priority: Priority
    status: TaskStatus
    created_at: datetime
    description: Optional[str] = None
    assignee_id: Optional[str] = None

    def __post_init__(self):
        # Invariante: title no vacío
        if not self.title or self.title.strip() == "":
            raise ValueError("Title cannot be empty")

        # Invariante: estado inicial siempre OPEN
        if self.status != TaskStatus.OPEN:
            raise ValueError("Initial status must be OPEN")