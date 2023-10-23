# Body, Request Body
from fastapi import Body, FastAPI

# name age gender creation....
app = FastAPI()


@app.post("/users")
async def creaate_user(name: str = Body(...), age: int = Body(...)):
    # payload
    return {"name": name, "age": age}

