from sqlalchemy import Boolean, Column, Integer, String

from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Integer, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    books = Column(String)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    img_url = Column(String, default="")
