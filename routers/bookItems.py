from fastapi import APIRouter, Form

router = APIRouter()

allBooks = []

@router.post("/books/add", tags=['books'])
def addNewBook(name: str = Form(...), description : str = Form(...)):
    allBooks.append({
        'name': name,
        'description': description
    })
    return {"message": "new book added with name {}".format(name)}

@router.get("/books/all", tags=['books'])
def viewBooks():
    return {"message": allBooks}

