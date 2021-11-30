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



