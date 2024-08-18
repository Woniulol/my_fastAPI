from fastapi import FastAPI
import uvicorn


# client -> uvicorn -> web framework (FastAPI)
app = FastAPI()

# tags, summary, description will all show up in the native docs supported by FastAPI
# e.g. <HOST>:<PORT>/docs
@app.post(
        path="/items",
        tags=["A sample tag to the endpoint"],
        summary="A high level summary",
        description="A detailed description of the Endpoint",
        response_description="A detailed description in the response content",
        deprecated=False
)
async def test():
    return {"items": "One item"}

@app.post("/")
async def post():
    return {"msg": "POST"}

@app.get("/")
async def get():
    return {"msg": "GET"}

@app.put("/")
async def put():
    return {"msg": "PUT"}

@app.patch("/")
async def patch():
    return {"msg": "PATCH"}

@app.delete("/")
async def delete():
    return {"msg": "DELETE"}

@app.options("/")
async def options():
    return {"msg": "OPTIONS"}

@app.head("/")
async def head():
    return {"msg": "HEAD"}

# @app.trace("/")
# async def trace():
#     return {"msg": "TRACE"}


# Run the following command in shell to start server (if not run .py directly)
# uvicorn simple_fastapi:app --reload

# Default port is 8000

if __name__ == "__main__":
    uvicorn.run(
        app="path_operation_decorators_01:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )
