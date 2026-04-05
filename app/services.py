from app.models import TaskFactory, TaskEvent
from app.dtos import TaskCreateRequest
from app.policies import NotificationPolicy


class NotificationService:
    def __init__(self, policy: NotificationPolicy):
        self.policy = policy

    def send_notification(self, event: TaskEvent) -> None:
        if self.policy.should_notify(event):
            print(f"Notification sent for event: {event}")
        else:
            print(f"Notification ignored for event: {event}")


class TaskService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create_task(self, request: TaskCreateRequest):
        task = TaskFactory.create(
            title=request.title,
            description=request.description,
            priority=request.priority,
            assignee_id=request.assignee_id
        )

        self.notification_service.send_notification(TaskEvent.TASK_CREATED)
        return task