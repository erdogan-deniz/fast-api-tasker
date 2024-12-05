from data import engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Async session for work with a database:
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: a base class for working with models.
------------------------------------------------------------------------------------------------------------------------
    """

    pass


class TasksTable(Model):
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: a table entity of tasks.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        __tablename__:
            Description: The table name.
            Type: str.
            Necessity: Necessary.

        id:
            Description: The table primary key.
            Type: int.
            Necessity: Necessary.

        name:
            Description: The column name.
            Type: str.
            Necessity: Necessary.

        description:
            Description: The column description.
            Type: str | None.
            Necessity: Optional.
------------------------------------------------------------------------------------------------------------------------
    """

    __tablename__: str = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


async def create_tables() -> None:
    """
    The function creates the necessary tables.

    :return: None.
    """

    # Open database connection:
    async with engine.begin() as connection:
        # Create all inherited tables:
        await connection.run_sync(Model.metadata.create_all)


async def drop_tables() -> None:
    """
    The function drops all database tables.

    :return: None.
    """

    # Open database connection:
    async with engine.begin() as connection:
        # Drop all inherited tables:
        await connection.run_sync(Model.metadata.drop_all)
