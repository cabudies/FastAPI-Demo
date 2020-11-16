from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import schemas, crud
import deps

router = APIRouter()

@router.post("/add")
async def addNewBook(book: schemas.BookCreate = Depends(schemas.BookCreate.as_form), db: Session = Depends(deps.get_db)):
    success = False
    try:
        crud.add_book(db=db, book=book)
        success = True
    except Exception as e:
        print("Unable to process book")
        print(e)
    return success 

@router.get("/all")
def viewBooks(db: Session = Depends(deps.get_db)):
    allBooks = crud.get_books(db=db)
    return {"message": allBooks}

