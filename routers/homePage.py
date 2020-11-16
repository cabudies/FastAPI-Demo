from fastapi import APIRouter

router = APIRouter()

@router.get("/") ## get route
def read_root(): ## function that gets called for "/" route
    return {"message": "Hello World"} ## return json response by default
