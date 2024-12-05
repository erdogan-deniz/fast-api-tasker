from sqlalchemy import select
from schema import STaskAdd, STaskGet
from database import new_session, TasksTable


# Pattern repository:
class TaskRepository:
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: A class for working with a database.
------------------------------------------------------------------------------------------------------------------------
    Class methods:
------------------------------------------------------------------------------------------------------------------------
    add_task:
            Description: The method adds a task to the database.
            Parameters: task - example of a task.
            Parameters type: STaskAdd.
            Returns: An ID of an added task.
            Return type: int.

    get_tasks:
            Description: The method returns all tasks in a list.
            Returns: Existing tasks.
            Return type: list[STaskGet].
------------------------------------------------------------------------------------------------------------------------
    """

    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        """
        The method adds a task to the database.

        :param task: Example of a task.

        :return: An ID of an added task.
        """

        async with new_session() as session:
            # Convert to python dict:
            task_dict = task.model_dump()
            task = TasksTable(**task_dict)

            # Add to the database:
            session.add(task)

            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def get_tasks(cls) -> list[STaskGet]:
        """
        The method adds a task to the database.

        :return: Existing tasks.
        """

        async with new_session() as session:
            query = select(TasksTable)

            # Make async query:
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskGet.model_validate(task_model) for task_model in task_models]

            return task_schemas
