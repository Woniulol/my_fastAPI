from fastapi import APIRouter, Request

app06 = APIRouter()

@app06.post("/request_object")
async def request_object(request: Request):
    return {
        "url": request.url,
        "ip": request.client.host,
        "headers": request.headers,
        "user-agent": request.headers.get("user-agent"),
        "app": request.app.title
    }