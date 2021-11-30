from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True


class UpdatePost(BaseModel):
    published: bool
