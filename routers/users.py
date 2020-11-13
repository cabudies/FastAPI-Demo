from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{name}", tags=['users']) ## parameterized route
def value(name: str): ## parameter, datatype
    return {"message" : "hello user {}".format(name)}