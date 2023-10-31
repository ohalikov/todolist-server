from typing import Union, List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from logging.config import dictConfig
from logs.my_log_conf import log_config
import logging

dictConfig(log_config)

class Todo(BaseModel):
    id: int
    text: str
    completed: bool


app = FastAPI(debug=True)


@app.get("/old")
def read_root(todos: List[Todo] = None):
    text_todo = [todo.text for todo in todos]
    logger = logging.getLogger('foo-logger')
    logger.debug('test')
    return {"text_todo": 'dffffff'}


@app.get("/")
def root():
    logger = logging.getLogger('foo-logger')
    logger.debug('This is test 2')
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__": 
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()