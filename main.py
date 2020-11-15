from fastapi import FastAPI, Request, Response ## fast api
import uvicorn ## uvicorn server to run the app
from fastapi.middleware.cors import CORSMiddleware ## add cors middleware

from origins import origins ## origins for cors
import routers ## custom routers
from db.database import SessionLocal

app = FastAPI(debug=True) ## run app in debug mode

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency middleware
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response

app.include_router(routers.api_router)

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000,
        reload=True ## need this reload to reload app after every change
    )
