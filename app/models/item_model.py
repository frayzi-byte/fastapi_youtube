from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Item(Base):
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)