from pydantic import BaseModel


class ItemsSchemaIn(BaseModel):
    title: str
    description: str = None


class ItemsSchema(ItemsSchemaIn):
    id: int


class UserSchemaIn(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str


class LoginSchema(BaseModel):
    username: str
    password: str
