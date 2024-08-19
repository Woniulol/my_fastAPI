from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr


app07 = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

@app07.post("/create_user", response_model=UserOut)
def create_user(user: UserIn):
    return user