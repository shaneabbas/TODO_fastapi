from db_todo_app.Schemas import LoginSchema
from fastapi import APIRouter, status, HTTPException
from db_todo_app.db import database, User
from passlib.hash import pbkdf2_sha256

router = APIRouter(
    tags=["Auth"]
)


@router.post('/login/', summary="Performs authentication")
async def login(request: LoginSchema):
    """
                        Performs authentication and returns the authentication token to keep the user
                        logged in for longer time.

                        Provide **Username** and **Password** to log in.

    """
    query = User.select().where(User.c.username == request.username)
    myuser = await database.fetch_one(query=query)

    if not myuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    if not pbkdf2_sha256.verify(request.password, myuser.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="password is not correct")

    return myuser
