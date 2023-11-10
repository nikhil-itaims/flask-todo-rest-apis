""" It has the model class which is stored the Todo's data.
"""
from app import db
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import TINYINT
from app.helpers.helper import get_current_datetime


class Todo(db.Model):
    __tablename__ = 'todos'

    id = sa.Column(TINYINT(1), primary_key=True)
    todo_name = sa.Column(sa.String(500), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, 
                           default=get_current_datetime)
    updated_at = sa.Column(sa.DateTime, default=None,
                           onupdate=get_current_datetime)
    
    def __init__(self, todo_name):
        self.todo_name = todo_name
