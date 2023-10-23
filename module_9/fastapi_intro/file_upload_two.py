from fastapi import FastAPI, File, UploadFile # https://fastapi.tiangolo.com/tutorial/request-files/?h=file

app = FastAPI()


@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}




