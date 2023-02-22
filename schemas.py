# Import BaseModel class
from pydantic import BaseModel

# Define your schema here.

class Item(BaseModel):
    task: str