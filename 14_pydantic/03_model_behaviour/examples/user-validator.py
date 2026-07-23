from pydantic import BaseModel , field_validator , model_validator, computed_field
from typing import List, Dict, Optional

class User(BaseModel):
    username:str

    @field_validator('username')
    def validate_username(cls, value:str):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return value

user = User(username="kul")

print(user)


class SignupData(BaseModel):
    password : str
    confirm_password : str

    @field_validator('password', 'confirm_password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    
signup = SignupData(password='password', confirm_password='password')
print(signup)


class Product(BaseModel):
    price : float
    quantity : int

    @computed_field
    @property
    def total_price(self) -> float :
        return self.price * self.quantity


product_data = Product(price=10, quantity=10)
print(product_data.total_price)