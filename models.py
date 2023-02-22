# Import sqlalchemy class
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
# Import Base class from database.py
from database import Base

# Create your models here.

class Item(Base): # 
    # tablename
    __tablename__ = 'items'

    # attributes
    id = Column(Integer, primary_key=True)
    task = Column(String(255))