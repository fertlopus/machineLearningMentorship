from fastapi import FastAPI, Path # title, description, deprecated

app = FastAPI()

# ge -> greater or equal
# gt -> greater than
# lt -> less than
# le -> less or equal


@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}


# @app.get("/license-plates/{license}")
# async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
#     return {"licence": license}

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-w{1}")):
    return {"licence": license}
