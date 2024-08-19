from fastapi import APIRouter, Form


app04 = APIRouter()

# Content-Type will be form-urlencoded
@app04.post("/regin")
async def data(
    username: str = Form(),
    password: str = Form(),
):
    print("username", username)
    print("password", password)
    return username