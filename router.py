from typing import Annotated
from repository import TaskRepository
from fastapi import APIRouter, Depends
from schema import STaskAdd, STaskGet, STaskId

# Add router for requests:
router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    """
    Function for adding tasks to a database.

    :param task: The being sent task.

    :return: ID of the saved task.
    """

    # Add task to 'db':
    task_id = await TaskRepository.add_task(task)

    # Status of request:
    return {"Status": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STaskGet]:
    """
    Function to get all existing tasks.

    :return: Existing tasks.
    """

    tasks = await TaskRepository.get_tasks()

    return {"tasks": tasks}
