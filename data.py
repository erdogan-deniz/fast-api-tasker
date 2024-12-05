from sqlalchemy.ext.asyncio import create_async_engine

# An engine for transactions:
engine = create_async_engine(
    # A database name + a driver + a table name:
    "sqlite+aiosqlite:///tasks.db"
)
