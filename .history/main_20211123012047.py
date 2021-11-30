from fasapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': "Hell world"}
