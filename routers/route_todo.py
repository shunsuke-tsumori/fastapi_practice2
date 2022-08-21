from fastapi import APIRouter, Request, Response, status, HTTPException
from fastapi.encoders import jsonable_encoder

from database import db_create_todo
from schemas import Todo, TodoBody

router = APIRouter()


@router.post("/api/todo", response_model=Todo)
async def create_todo(request: Request, response: Response, data: TodoBody):
    todo = jsonable_encoder(data)
    res = await db_create_todo(todo)
    response.status_code = status.HTTP_201_CREATED
    if res:
        return res
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Create task failed")
