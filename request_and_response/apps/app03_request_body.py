from datetime import date
from typing import Union, List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator

test_param = "123"

class User(BaseModel):
    name: str
    age: int = Field(default=0, gt=0, lt=100)
    birth: Optional[date] = None
    friends: List[int]  # Filed required.
    description: Optional[str] = None

    # If the validation provided by type hint or Field is not enough, you may define it yourself
    @field_validator("name")
    @classmethod
    def name_must_alpha(cls, value: str):
        assert value.isalpha(), "<name> must be alpha"
        # must return the value
        return value

class Data(BaseModel):
    data: List[User]


app03 = APIRouter()

@app03.post("/user")
async def user(user: User):
    print(user, type(user))
    print(user.model_dump())
    return {"msg": "user"}

@app03.post("/data")
async def data(data: Data, test_param: str = test_param):
    print(test_param)
    print(data, type(data))
    print(data.model_dump())
    return {"msg": "data"}
