from fastapi import FastAPI, Form ## fast api
import uvicorn ## uvicorn server to run the app

app = FastAPI(debug=True) ## run app in debug mode

allBooks = []

@app.get("/") ## get route
def read_root(): ## function that gets called for "/" route
    print("root")
    return {"message": "Hello World"} ## return json response by default

@app.get("/user/{name}") ## parameterized route
def value(name: str): ## parameter, datatype
    return {"message" : "hello user {}".format(name)}

@app.post("/addBook")
def addNewBook(name: str = Form(...), description : str = Form(...)):
    allBooks.append({
        'name': name,
        'description': description
    })
    return {"message": "new book added with name {}".format(name)}

@app.get("/viewBooks")
def viewBooks():
    return {"message": allBooks}

if __name__ == "__main__":
    uvicorn.run(
        'main:app', 
        host="0.0.0.0", 
        port=8000, 
        reload=True ## need this reload to reload app after every change
    )