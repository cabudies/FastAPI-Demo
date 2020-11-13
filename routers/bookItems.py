from fastapi import APIRouter, Form

router = APIRouter()

allBooks = []

@router.post("/add")
def addNewBook(name: str = Form(...), description : str = Form(...)):
    allBooks.append({
        'name': name,
        'description': description
    })
    return {"message": "new book added with name {}".format(name)}

@router.get("/all")
def viewBooks():
    return {"message": allBooks}

