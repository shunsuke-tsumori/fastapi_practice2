from typing import Optional

from pydantic import BaseModel


class TodoBody(BaseModel):
    title: str
    description: str


class Todo(TodoBody):
    id: str
    title: str
    description: str


class SuccessMsg(BaseModel):
    message: str


class UserBody(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    id: Optional[str] = None
    email: str
