from pydantic import BaseModel
from typing import Optional

from schemas.menu import MenuBase


class RestaurantBase(BaseModel):
    name: str
    type: str
    image_cover: str
    isOpen: bool


class RestaurantCreate(RestaurantBase):
    # menus: Optional[MenuBase] = None

    class Config:
        orm_mode = True

class RestaurantPatch(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    image_cover: Optional[str] = None
    isOpen: Optional[bool] = None

    class Config:
        orm_mode = True

class RestaurantRead(RestaurantBase):
    id: int


class Restaurant(RestaurantBase):
    id: int

    class Config:
        orm_mode = True