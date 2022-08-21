from typing import Optional

from pydantic import BaseModel
from decouple import config

CSRF_KEY = config("CSRF_KEY")
class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY

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

class Csrf(BaseModel):
    csrf_token: str