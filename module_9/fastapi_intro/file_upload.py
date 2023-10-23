from fastapi import FastAPI, File # https://fastapi.tiangolo.com/tutorial/request-files/?h=file

app = FastAPI()


@app.post("/files")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}

