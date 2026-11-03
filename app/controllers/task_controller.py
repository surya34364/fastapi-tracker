from fastapi import APIRouter, HTTPException
from app.models.task_model import TaskModel
from app.views.task_views import TaskListResponse, TaskResponse, TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=TaskListResponse)
def list_tasks():
    data = TaskModel.get_all()
    return {"count": len(data), "tasks": data}

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = TaskModel.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(payload: TaskCreate):
    return TaskModel.create(title=payload.title)