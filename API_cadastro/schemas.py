from typing import List
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Item] = []


