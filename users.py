from db_todo_app.Schemas import UserSchemaIn, UserSchema
from typing import List
from fastapi import APIRouter, status, HTTPException
from db_todo_app.db import database, User
from passlib.hash import pbkdf2_sha256

router = APIRouter(
    tags=["Users"]
)


@router.post('/users/', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def create_user(user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    query = User.insert().values(username=user.username, password=hashed_password)
    last_record_id = await database.execute(query)

    return {**user.dict(), "id": last_record_id}


@router.get('/users/', response_model=List[UserSchema])
async def get_users():
    query = User.select()

    return await database.fetch_all(query=query)
