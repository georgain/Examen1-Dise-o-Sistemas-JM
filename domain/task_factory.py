from datetime import datetime
import uuid

from domain.task import Task
from domain.task_status import TaskStatus
from domain.priority import Priority


class TaskFactory:

    @staticmethod
    def create(
        title: str,
        priority: Priority,
        description: str = None,
        assignee_id: str = None
    ) -> Task:

        # Validaciones (reglas de negocio)
        if not title or title.strip() == "":
            raise ValueError("Title is required")

        if priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
            raise ValueError("Invalid priority")

        # Creación consistente
        return Task(
            id=str(uuid.uuid4()),
            title=title,
            priority=priority,
            status=TaskStatus.OPEN,  # siempre OPEN al inicio
            created_at=datetime.utcnow(),
            description=description,
            assignee_id=assignee_id
        )