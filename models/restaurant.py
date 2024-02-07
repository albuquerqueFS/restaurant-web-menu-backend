from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import Base

from .menu import Menu

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    image_cover = Column(String)
    isOpen = Column(Boolean)

    menus = relationship("Menu", back_populates="restaurant", cascade="all, delete-orphan")