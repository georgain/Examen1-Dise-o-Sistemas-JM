from fastapi import FastAPI, status

from app.dtos import TaskCreateRequest, TaskResponse
from app.policies import AlwaysNotify
from app.services import NotificationService, TaskService

app = FastAPI()

notification_service = NotificationService(policy=AlwaysNotify())
task_service = TaskService(notification_service=notification_service)


@app.get("/")
def home():
    return {"message": "Task API is running"}


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(request: TaskCreateRequest):
    task = task_service.create_task(request)

    return TaskResponse(
        id=task.id,
        title=task.title,
        priority=task.priority,
        status=task.status,
        created_at=task.created_at
    )