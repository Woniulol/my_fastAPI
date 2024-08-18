from fastapi import APIRouter

user = APIRouter()

@user.get("/user/login")
def user_login():
    return {"user": "login"}

@user.get("/user/reg")
def user_reg():
    return {"user": "reg"}

if __name__ == "__main__":
    ...
