from pydantic import BaseModel
from typing import List

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

class TaskListResponse(BaseModel):
    count: int
    tasks: List[TaskResponse]