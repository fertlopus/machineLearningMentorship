from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}


@app.get("/cookie")
async def custom_cookie(response: Response):
    response.set_cookie("cookie_name", "cookie-value", max_age=1000)
    return {"hello": "world"}