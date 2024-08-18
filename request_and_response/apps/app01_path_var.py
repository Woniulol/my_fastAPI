from fastapi import APIRouter


app01 = APIRouter()

# the parameters in the path must also show in the path operation function parameters.
@app01.get("/user/{id}")
def get_user(id: str):
    print("id", id, type(id))
    return {"user_id": id}

# An interesting case.
# This wil never be triggered.
# Because the definition sequence of the router matters.
@app01.get("/user/1")
def get_root_user():
    return {"user_id": "root"}