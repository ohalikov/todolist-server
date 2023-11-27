# from datetime import datetime
import uuid
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
# from app.oauth2 import require_user


router = APIRouter()


# Get all todos
# @router.get('/', response_model=schemas.ListTodoResponse)
# def get_todos(
#         db: Session = Depends(get_db), limit: int = 10, page: int = 1,
#         search: str = '', user_id: str = Depends(require_user)):
#     skip = (page - 1) * limit

#     todos = db.query(models.Todo).group_by(models.Todo.id).filter(
#         models.Todo.text.contains(search)).limit(limit).offset(skip).all()
#     return {
#         'status': 'success',
#         'results': len(todos),
#         'todos': todos
#     }
@router.get('/', response_model=schemas.ListTodoResponse)
def get_todos(
        db: Session = Depends(get_db), limit: int = 10, page: int = 1,
        search: str = ''):
    skip = (page - 1) * limit

    todos = db.query(models.Todo).group_by(models.Todo.id).filter(
        models.Todo.todo_text.contains(search)).limit(limit).offset(skip).all()
    return {
        'status': 'success',
        'results': len(todos),
        'todos': todos
    }


# Create Todo
# @router.post('/', status_code=status.HTTP_201_CREATED,
#              response_model=schemas.TodoResponse)
# def create_todo(todo: schemas.CreateTodoSchema,
#                 db: Session = Depends(get_db),
#                 owner_id: str = Depends(require_user)):
#     todo.user_id = uuid.UUID(owner_id)
#     new_todo = models.Todo(**todo.dict())
#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)
@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.TodoResponse,
             response_model_exclude_unset=True
             )
def create_todo(todo: schemas.CreateTodoSchema,
                db: Session = Depends(get_db)):
    new_todo = models.Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# Update Todo
# @router.put('/{id}', response_model=schemas.TodoResponse)
# def update_todo(id: str, todo: schemas.UpdateTodoSchema,
#                 db: Session = Depends(get_db),
#                 user_id: str = Depends(require_user)):
#     todo_query = db.query(models.Todo).filter(models.Todo.id == id)
#     updated_todo = todo_query.first()

#     if not updated_todo:
#         raise HTTPException(status_code=status.HTTP_200_OK,
#                             detail=f'No todo with this id: {id} found')
#     if updated_todo.user_id != uuid.UUID(user_id):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail='You are not allowed to perform this action')
#     todo.user_id = user_id
#     todo_query.update(todo.dict(exclude_unset=True), synchronize_session=False)
#     db.commit()
#     return updated_todo
@router.put('/{id}', response_model=schemas.TodoResponse)
def update_todo(id: str, todo: schemas.UpdateTodoSchema,
                db: Session = Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id)
    updated_todo = todo_query.first()

    if not updated_todo:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No todo with this id: {id} found')

    todo_query.update(
        todo.model_dump(exclude_unset=True),
        synchronize_session=False
    )
    db.commit()
    return updated_todo


# Get a single Todo
# @router.get('/{id}', response_model=schemas.TodoResponse)
# def get_todo(id: str, db: Session = Depends(get_db),
#              user_id: str = Depends(require_user)):
#     todo = db.query(models.Todo).filter(models.Todo.id == id).first()
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"No todo with this id: {id} found")
#     return todo
@router.get('/{id}', response_model=schemas.TodoResponse)
def get_todo(id: str, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No todo with this id: {id} found")
    return todo


# Delete Todo
# @router.delete('/{id}')
# def delete_todo(id: str, db: Session = Depends(get_db),
#                 user_id: str = Depends(require_user)):
#     todo_query = db.query(models.Todo).filter(models.Todo.id == id)
#     todo = todo_query.first()
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'No todo with this id: {id} found')

#     if str(todo.user_id) != user_id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail='You`re not allowed to perform this action')
#     todo_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: str, db: Session = Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id)
    todo = todo_query.first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No todo with this id: {id} found')

    todo_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
