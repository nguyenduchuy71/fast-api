from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def root():
    return {'message': "Hell world"}


@app.get('/posts')
def get_posts():
    return {"data": "This is data"}


@app.post('/createposts')
def get_posts(payload: dict = Body(...)):
    print(payload)
    return {"new posr": f"title:{payload['title']}"}
