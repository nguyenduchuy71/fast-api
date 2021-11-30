from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

my_posts = [{"id": 1, "title": "title of post 1",
             "content": "content of post 1"}]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get('/')
def root():
    return {'message': "Hell world"}


@app.get('/posts')
def get_posts():
    return {"data": my_posts}


@app.post('/posts')
def get_posts(new_post: Post):
    my_posts.append(new_post.dict())
    return {"data": new_post}
