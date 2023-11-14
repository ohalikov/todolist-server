from datetime import datetime
import uuid
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
from app.oauth2 import require_user


router = APIRouter()


@router.get('/', response_model=schemas.ListTodoResponse)
def get_todos(
        db: Session = Depends(get_db), limit: int = 10, page: int = 1,
        search: str = '', user_id: str = Depends(require_user)
    ):
    skip = (page - 1) * limit

    todos = db.query(models.Todo).group_by(models.Todo.id).filter(
        models.Todo.text.contains(search)).limit(limit).offset(skip).all()
    return {
        'status': 'success', 
        'results': len(todos), 
        'todos': todos
    }