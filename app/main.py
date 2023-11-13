from typing import Union, List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Todo(BaseModel):
    # id: UUID = Field(default_factory=uuid4)
    text: str
    completed: bool


app = FastAPI(debug=True)

#       [
#         {
#           "id": 0,
#           "text": 'Learn the basics of Vue',
#           "completed": True,
#         },
#         {
#           "id": 1,
#           "text": 'Learn the basics of Typescript',
#           "completed": False,
#         },
#         {
#           "id": 2,
#           "text": 'Subscribe to the channel',
#           "completed": False,
#         },
#         {
#           "id": 3,
#           "text": 'Learn the basics of JS',
#           "completed": True,
#         },
#       ]

todos = {}


@app.get("/todos")
def read_todos():
    return todos


@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    todo_id = uuid4()
    todos[todo_id] = todo
    return todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: UUID, todo: Todo):
    todos[todo_id] = todo
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: UUID):
    todo = str(todos[todo_id])
    del todos[todo_id]
    return {'message': f'Item { {todo} } deleted'}


if __name__ == "__main__": 
    config = uvicorn.Config("main:app", port=5000, log_level="debug", reload=True)
    server = uvicorn.Server(config)
    server.run()