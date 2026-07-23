from pydantic import BaseModel

#Assignment: Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock: bool = True

