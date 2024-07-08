from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from .database import DATABASE_URL, engine, metadata
from .models import tasks

metadata.create_all(engine)

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool

@app.post("/tasks/")
async def create_task(task: Task):
    query = tasks.insert().values(title=task.title, description=task.description, completed=task.completed)
    await database.execute(query)
    return {"message": "Task created successfully"}

@app.get("/tasks/")
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    query = tasks.update().where(tasks.c.id == task_id).values(
        title=task.title, description=task.description, completed=task.completed)
    await database.execute(query)
    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": "Task deleted successfully"}
