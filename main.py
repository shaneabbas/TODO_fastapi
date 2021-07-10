
from fastapi import FastAPI
from db_todo_app.db import metadata, database, engine
import items
import users
import auth

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(auth.router)
