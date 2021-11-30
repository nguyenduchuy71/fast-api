from sqlalchemy import Column,Integer
from .database import Base


class Post(Base):
    __table_name__ = 'posts'
    id= Column(Integer,primary_key=True,nullable=False)
