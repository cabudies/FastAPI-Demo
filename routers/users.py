from fastapi import APIRouter
from sqlalchemy.orm import Session

from db import schemas, crud, models
from db.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Request, Response

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/{name}") ## parameterized route
def value(name: str): ## parameter, datatype
    return {"message" : "hello user {}".format(name)}

# @router.post("/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)