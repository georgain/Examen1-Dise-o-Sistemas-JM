from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid


class TaskStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TaskEvent(str, Enum):
    TASK_CREATED = "TASK_CREATED"
    STATUS_CHANGED = "STATUS_CHANGED"
    TASK_DONE = "TASK_DONE"


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
        if not self.title or self.title.strip() == "":
            raise ValueError("Title cannot be empty")

        if self.priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
            raise ValueError("Invalid priority")

        if self.status != TaskStatus.OPEN:
            raise ValueError("Initial status must be OPEN")


class TaskFactory:
    @staticmethod
    def create(
        title: str,
        priority: Priority,
        description: Optional[str] = None,
        assignee_id: Optional[str] = None
    ) -> Task:
        if not title or title.strip() == "":
            raise ValueError("Title is required")

        if priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
            raise ValueError("Invalid priority")

        return Task(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            priority=priority,
            status=TaskStatus.OPEN,
            assignee_id=assignee_id,
            created_at=datetime.utcnow()
        )