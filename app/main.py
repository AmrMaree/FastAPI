from random import randrange
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Response, status, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import user, post

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='scjo?m4r', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
    "title": "my favourite food", "content": "i like pizza", "id": 2}]

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "welcome to my api!"}
