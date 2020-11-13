from fastapi import FastAPI ## fast api
import uvicorn ## uvicorn server to run the app
from fastapi.middleware.cors import CORSMiddleware ## add cors middleware

from origins import origins ## origins for cors
import routers ## custom routers

app = FastAPI(debug=True) ## run app in debug mode

@app.get("/") ## get route
def read_root(): ## function that gets called for "/" route
    return {"message": "Hello World"} ## return json response by default

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.api_router)

if __name__ == "__main__":
    uvicorn.run(
        'main:app', 
        host="0.0.0.0", 
        port=8000, 
        reload=True ## need this reload to reload app after every change
    )