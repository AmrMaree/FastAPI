from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
    "title": "my favourite food", "content": "i like pizza", "id": 2}]

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "welcome to my api!"}
