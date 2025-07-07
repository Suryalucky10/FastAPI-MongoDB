from fastapi import APIRouter
from models.todos import Todo
from config.database import coll_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()
@router.get("/")
async def get_todos():
    todos=list_serial(coll_name.find())
    return todos
@router.post("/")
async def post_todo(todo:Todo):
    coll_name.insert_one(dict(todo))
@router.put("/{id}")
async def put_todo(id:str, todo:Todo):
    coll_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})

@router.delete("/{id}")
async def delete_todo(id:str):
    coll_name.find_one_and_delete({"_id":ObjectId(id)})