from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.menu import Menu as MenuModel
from models.restaurant import Restaurant as RestaurantModel
from dtos.menu import MenuPatch

def get_menu(id: int, db: Session):
    menus = db.query(MenuModel).filter(MenuModel.id == id).first()
    return menus

def get_menus(db: Session):
    menus = db.query(MenuModel).all()
    return menus

def create_menu(db: Session, restaurant_id: int, menu: MenuModel):
    restaurant = db.query(RestaurantModel).filter(RestaurantModel.id == restaurant_id).first()
    db.add(menu)
    db.commit()
    return menu

def update_menu(id: int, db: Session, updated_data: MenuPatch):
    menu = db.query(MenuModel).filter(MenuModel.id == id).first()

    if menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")

    menu_updated = updated_data.dict(exclude_unset=True)
    for key, value in menu_updated.items():
        setattr(menu, key, value)

    db.commit()
    db.refresh(menu)
    return menu
