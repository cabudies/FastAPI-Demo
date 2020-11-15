from fastapi import APIRouter, Form, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from db import schemas, crud
from db.database import SessionLocal, engine

router = APIRouter()

allBooks = []

# Dependency
def get_db(request: Request):
    # return request.state.db
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/add")
# def addNewBook(name: str = Form(...), description : str = Form(...)):
#     allBooks.append({
#         'name': name,
#         'description': description
#     })
#     return {"message": "new book added with name {}".format(name)}

@router.post("/add")
# def addNewBook(book: schemas.BookCreate, db: Session = Depends(crud.get_db)):
async def addNewBook(book: schemas.BookCreate = Depends(schemas.BookCreate.as_form), db: Session = Depends(get_db)):
# async def addNewBook(request: Request):
    # db_book = crud.book(db, book)
    # if db_book:
    #     raise HTTPException(status_code=400, detail="Could not add new book")
    success = False
    try:
        # book = await request.form()
        # print("book==", book)
        # db = Depends(crud.get_db)
        crud.add_book(db=db, book=book)
        success = True
    except Exception as e:
        print("Unable to process book")
        print(e)
    return success 

@router.get("/all")
def viewBooks():
    return {"message": allBooks}

