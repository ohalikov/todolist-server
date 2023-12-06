# validate the requests and responses.
from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    photo: str

    class Config:
        # orm_mode = True
        from_attributes = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    role: str = 'user'
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class FilteredUserResponse(UserBaseSchema):
    id: uuid.UUID


class TodoBaseSchema(BaseModel):
    todo_text: str
    completed: bool
    # user_id: uuid.UUID | None = None

    class Config:
        from_attributes = True


class TodoResponse(TodoBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    # user: FilteredUserResponse


class CreateTodoSchema(TodoBaseSchema):
    pass


class UpdateTodoSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    # user_id: uuid.UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class ListTodoResponse(BaseModel):
    status: str
    results: int
    todos: List[TodoResponse]
