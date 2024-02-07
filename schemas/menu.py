from pydantic import BaseModel


class MenuBase(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str
    restaurant_id: int
