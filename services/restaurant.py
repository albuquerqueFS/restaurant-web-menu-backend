from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.restaurant import Restaurant as RestaurantModel
from models.user import User
from schemas.restaurant import Restaurant as RestaurantSchema, RestaurantPatch

def get_restaurant(id: int, db: Session):
    restaurants = db.query(RestaurantModel).filter(RestaurantModel.id == id).first()
    return restaurants

def get_restaurants(db: Session):
    restaurants = db.query(RestaurantModel).all()
    return restaurants

def create_restaurant(db: Session, restaurant: RestaurantModel):
    db.add(restaurant)
    db.commit()
    return restaurant

def update_restaurant(id: int, db: Session, updated_data: RestaurantPatch):
    restaurant = db.query(RestaurantModel).filter(RestaurantModel.id == id).first()

    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    restaurant_updated = updated_data.dict(exclude_unset=True)
    for key, value in restaurant_updated.items():
        setattr(restaurant, key, value)

    db.commit()
    db.refresh(restaurant)
    return restaurant
