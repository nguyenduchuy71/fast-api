from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': "Hell world"}


@app.get('/posts')
def get_posts():
    return {"data": "This is data"}
