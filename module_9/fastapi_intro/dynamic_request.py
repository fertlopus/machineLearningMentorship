from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{id}")
async def get_user(id: int):
    return {"id": id}
