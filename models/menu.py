from sqlalchemy import Integer, Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))

    # Use string reference for Restaurant
    restaurant = relationship("Restaurant", back_populates="menus")
