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