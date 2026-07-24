from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address
    createdAt: datetime
    tags: List[str] = []
    is_active : bool = True

    model_config = ConfigDict(
        json_encoders={datetime : lambda v: v.strftime("%Y-%m-%d %H:%M:%S")}
    )
        


address = Address(
    street = "123 something",
    city = "Jaipur",
    postal_code = "302001",
)

user = User(
    id= 1,
    name= "Kuldeep",
    address = address,
    createdAt = datetime.now(),
    tags = ["python", "pydantic", "serialization"],
)


# Using model_dump() -> dict

python_dict = user.model_dump()
print(f"Python dict: {python_dict}")

print("\n========================\n")


# Using model_dump_json() -> str

python_dict_json = user.model_dump_json()
print(f"Python dict json: {python_dict_json}")

print("\n========================\n")


# Using model_dump_json() with indent parameter -> str
# indent parameter is used to pretty print the json
# indent used for add space between the json elements and make the json readable
python_dict_json = user.model_dump_json(indent=4)
print(f"Python dict json with indentation: {python_dict_json}")

print("\n========================\n")

