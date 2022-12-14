from typing import List

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    name: str
    password: str
    email: str

    class Config:
        orm_mode = True
