from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


class PublicPost(BaseModel):
    title: str


app = FastAPI()

# Pseudo Database:
posts = {
    1: Post(title="Machine Learning", nb_views=10000),
}


@app.get("/posts/{id}", response_model=PublicPost)
async def get_post(id: int):
    return posts[id]
