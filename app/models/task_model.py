from typing import Dict, List, Optional

tasks_db: Dict[int, dict] = {
    1: {"id": 1, "title": "Buy groceries", "completed": False},
    2: {"id": 2, "title": "Learn Git commands", "completed": False},
}

class TaskModel:
    @staticmethod
    def get_all() -> List[dict]:
        return list(tasks_db.values())

    @staticmethod
    def get_by_id(task_id: int) -> Optional[dict]:
        return tasks_db.get(task_id)

    @staticmethod
    def create(title: str) -> dict:
        new_id = max(tasks_db.keys(), default=0) + 1
        new_task = {"id": new_id, "title": title, "completed": False}
        tasks_db[new_id] = new_task
        return new_task