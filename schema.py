from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: A class of task to add to the database.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        name:
            Description: The name of a task.
            Type: str.
            Necessity: Necessary.

        description:
            Description: The description of a task.
            Type: str | None.
            Necessity: Optional.
------------------------------------------------------------------------------------------------------------------------
    """

    name: str
    description: str | None = None


class STaskGet(STaskAdd):
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: A class of task to get from a database.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        id:
            Description: The primary key of a task.
            Type: int.
            Necessity: Necessary.
------------------------------------------------------------------------------------------------------------------------
    """

    id: int

    # Take value to a python type:
    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: A class of answer of task adding.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        task_id:
            Description: The primary key of a task which has been added.
            Type: int.
            Necessity: Necessary.

        status:
            Description: The status of task adding.
            Type: bool.
            Necessity: Optional.
            Default value: True.
------------------------------------------------------------------------------------------------------------------------
    """

    task_id: int
    status: bool = True
