from fastapi import APIRouter

from routers import bookItems, users, homePage

api_router = APIRouter()

api_router.include_router(homePage.router)
api_router.include_router(bookItems.router, prefix='/books', tags=['books'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
