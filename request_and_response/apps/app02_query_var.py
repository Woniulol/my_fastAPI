from typing import Union

from fastapi import APIRouter


app02 = APIRouter()

"""
When a path operation function declares parameters that are not
path parameters, those parameters will be automatically interpreted
as inquiry parameters in key-value pair form.

(all the parameters after ? in URL and separated by &)
"""
@app02.get("/jobs")
async def get_jobs(name: str, years: Union[int, str], pay: int):
    print(type(years))  # str
    return {"msg": f"job info {name, years, pay}"}

"""
Use path parameter and query parameter at the same time
"""
@app02.get("/jobs_2/{name}")
async def get_jobs_2(name: str, years: int, pay: int):
    return {"msg": f"job info {name, years, pay}"}
