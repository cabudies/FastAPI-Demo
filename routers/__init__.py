from fastapi import APIRouter

from routers import bookItems, users

api_router = APIRouter()

api_router.include_router(bookItems.router, prefix='/books', tags=['books'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
