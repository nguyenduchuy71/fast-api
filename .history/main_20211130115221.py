from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import post, user, auth, vote
from config import settings
# models.Base.metadata.create_all(bind=engine)
print(settings.database_name)
app = FastAPI()
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return {'message': "Hello, welcome to FastAPI"}
