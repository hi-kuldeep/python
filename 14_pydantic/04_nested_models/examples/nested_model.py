from typing import List, Optional
from pydantic import BaseModel 

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None


# if we not use this then we get error because comment is not defined yet so we use this to define comment
# same as the forward reference in c++

Comment.model_rebuild()


address = Address(
    street = "123 something",
    city = "Jaipur",
    postal_code = "302001",
)

user = User(
    id= 1,
    name= "Kuldeep",
    address = address,
)

comment = Comment(
    id=1,
    content="First Comment",
    replies = [
        Comment(id=2, content="Reply on first comment"),
        Comment(id=3, content="Reply on first comment 2")
    ]
)