from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool


input_data = {
    'id' : 101,
    'name' : "kuldeep kumawat",
    'is_active' : True
}