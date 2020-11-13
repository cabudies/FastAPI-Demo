from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}") ## parameterized route
def value(name: str): ## parameter, datatype
    return {"message" : "hello user {}".format(name)}