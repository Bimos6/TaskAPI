from schemas.task import TaskCreate, TaskResponse


class TaskNotFoundError(Exception):
    pass


class TaskService:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def create(self, dto: TaskCreate) -> TaskResponse:
        task = {
            "id": self._next_id,
            "title": dto.title,
            "description": dto.description,
            "status": dto.status.value,
        }
        self._tasks.append(task)
        self._next_id += 1
        return TaskResponse(**task)

    def get_all(self) -> list[TaskResponse]:
        return [TaskResponse(**t) for t in self._tasks]

    def get_by_id(self, task_id: int) -> TaskResponse:
        for t in self._tasks:
            if t["id"] == task_id:
                return TaskResponse(**t)
        raise TaskNotFoundError(f"Задача {task_id} не найдена")