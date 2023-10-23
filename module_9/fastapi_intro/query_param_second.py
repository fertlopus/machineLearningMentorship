from fastapi import FastAPI, Path, Query
from enum import Enum

app = FastAPI()


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format": format}
