from abc import ABC, abstractmethod
from app.models import TaskEvent


class NotificationPolicy(ABC):
    @abstractmethod
    def should_notify(self, event: TaskEvent) -> bool:
        pass


class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: TaskEvent) -> bool:
        return event in [
            TaskEvent.TASK_CREATED,
            TaskEvent.STATUS_CHANGED,
            TaskEvent.TASK_DONE
        ]


class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: TaskEvent) -> bool:
        return event == TaskEvent.TASK_DONE