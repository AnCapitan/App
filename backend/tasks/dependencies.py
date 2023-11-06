from .service import TasksRepository, TasksService


def tasks_service():
    return TasksService(TasksRepository)