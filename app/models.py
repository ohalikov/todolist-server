import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4())
    text = Column(String, nullable=False)
    completed = Column
    