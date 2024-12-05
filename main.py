from fastapi import FastAPI
from router import router as task_router
from contextlib import asynccontextmanager
from database import create_tables, drop_tables


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    """
    The function creates a context to work with application.

    :param app: A FastAPI application.

    :return: None.
    """

    await drop_tables()
    print("The tables have been dropped!")
    await create_tables()
    print("The tables have been created!")
    yield
    print("Shut down application...")

# Create an application:
app = FastAPI(lifespan=lifespan)

# Add a router to the application:
app.include_router(task_router)
