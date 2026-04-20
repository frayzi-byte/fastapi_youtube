from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Item(Base):
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String, nullable=False)