from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
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


@app.get('/posts/{id}')
def get_post(id):
    return {"data": my_posts}

@app.post('/posts')
def get_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": post_dict}
