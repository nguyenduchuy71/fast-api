from pydantic import BaseModel
from fastapi import FastAPI, status, Response, HTTPException, Depends
from typing import Optional, List
from psycopg2.extras import RealDictCursor
import psycopg2
import time
import models
import schemas
import utils
from database import engine, get_db
from sqlalchemy.orm.session import Session


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='18066791', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error:", error)
        time.sleep(2)


@app.get('/')
def root():
    return {'message': "Hello, welcome to FastAPI"}


@app.get('/posts', response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.get('/posts/{id}', response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()
    # print(post)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    return post


@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(new_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (new_post.title, new_post.content, new_post.published))
    # post = cursor.fetchone()
    # conn.commit()
    post = models.Post(title=new_post.title,
                       content=new_post.content, published=new_post.published)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    # delete_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}', response_model=schemas.Post)
def update_post(id: int, update_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    # new_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} not found")
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash password
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with {id} not found')
