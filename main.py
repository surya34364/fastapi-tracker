from fastapi import FastAPI
from app.controllers.task_controller import router as task_router

app = FastAPI(title="Task Tracker MVC")
app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Tracker v1.0"}

@app.get("/")
def home():
    return {"status": "online", "message": "FastAPI Tracker is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "FastAPI Tracker is healthy"}