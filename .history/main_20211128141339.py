from fastapi import FastAPI
import models
from database import engine
from routers import post, user, auth
from pydantic import BaseSettings
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


class Settings(BaseSettings):
    database_password: str
    database_username: str = "postgres"
    secret_key: str = "18066791"


settings = Settings()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return {'message': "Hello, welcome to FastAPI"}
