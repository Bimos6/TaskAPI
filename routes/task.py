from fastapi import APIRouter, Depends, HTTPException
from schemas.task import TaskCreate, TaskResponse
from services.task import TaskService, TaskNotFoundError

router = APIRouter(prefix="/tasks", tags=["tasks"])

_service = TaskService()


def get_service():
    return _service


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(body: TaskCreate, service: TaskService = Depends(get_service)):
    return service.create(body)


@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(service: TaskService = Depends(get_service)):
    return service.get_all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_service)):
    try:
        return service.get_by_id(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Задача {task_id} не найдена")