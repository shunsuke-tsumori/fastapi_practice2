from typing import List

from fastapi import APIRouter, Request, Response, status, HTTPException
from fastapi.encoders import jsonable_encoder

from database import db_create_todo, db_get_tools, db_get_single_todo, db_update_todo, db_delete_todo
from schemas import Todo, TodoBody, SuccessMsg

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


@router.get("/api/todo", response_model=List[Todo])
async def get_tools():
    return await db_get_tools()


@router.get("/api/todo/{id}", response_model=Todo)
async def get_single_tool(id: str):
    res = await db_get_single_todo(id)
    if res:
        return res
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task of ID:{id} doesn't exist")


@router.put("/api/todo/{id}", response_model=Todo)
async def update_todo(id: str, data: TodoBody):
    todo = jsonable_encoder(data)
    res = await db_update_todo(id, todo)
    if res:
        return res
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Update task failed")


@router.delete("/api/todo/{id}", response_model=SuccessMsg)
async def delete_todo(id: str):
    res = await db_delete_todo(id)
    if res:
        return {"message": "Successfully deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Delete task failed")
