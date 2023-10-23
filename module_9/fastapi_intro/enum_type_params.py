from fastapi import FastAPI
from enum import Enum


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


app = FastAPI()


@app.get("/user/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}
