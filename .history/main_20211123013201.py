from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get('/')
def root():
    return {'message': "Hell world"}


@app.get('/posts')
def get_posts():
    return {"data": "This is data"}


@app.post('/createposts')
def get_posts(new_post: Post):
    print(new_post)
    return {"message": f"new post"}
