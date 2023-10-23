from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


app = FastAPI()

# Pseudo Database:
posts = {
    1: Post(title="Machine Learning", nb_views=10000),
}

@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]
