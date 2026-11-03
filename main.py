from fastapi import FastAPI
from app.controllers.task_controller import router as task_router

app = FastAPI(title="Task Tracker MVC")
app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "API is online"}