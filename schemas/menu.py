from pydantic import BaseModel
from typing import Optional


class MenuBase(BaseModel):
    name: str
    description: str
    price: float
    image: str
    restaurant_id: int

class MenuCreate(MenuBase):
    class Config:
        orm_mode = True

class MenuPatch(MenuBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    restaurant_id: Optional[int] = None

    class Config:
        orm_mode = True

class MenuRead(MenuBase):
    id: int