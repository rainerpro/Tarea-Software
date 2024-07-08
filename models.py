from sqlalchemy import Table, Column, Integer, String, Boolean
from .database import metadata

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("description", String, index=True),
    Column("completed", Boolean, default=False)
)
