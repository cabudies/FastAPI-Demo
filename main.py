from fastapi import FastAPI ## fast api
import uvicorn ## uvicorn server to run the app

app = FastAPI() ## run app in debug mode

@app.get("/") ## get route
def read_root(): ## function that gets called for "/" route
    return {"message": "Hello World"} ## return json response by default

@app.get("/{name}") ## parameterized route
def value(name: str): ## parameter, datatype
    return {"message" : "hello user {}".format(name)}

if __name__ == "__main__":
    uvicorn.run(
        'main:app', 
        host="0.0.0.0", 
        port=8000, 
        reload=True ## need this reload to reload app after every change
    )