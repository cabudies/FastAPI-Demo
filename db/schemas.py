from typing import List
from fastapi import Form
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str
    img_url: str

    @classmethod
    def as_form(cls, title: str = Form(...), description: str = Form(...), img_url: str = Form(...)):
        return cls(title=title, description=description, img_url=img_url)


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    books: str

    class Config:
        orm_mode = True