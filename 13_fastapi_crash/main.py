from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    email: str
    is_active: bool = True

users : List[User]= []


@app.get("/")
def read_root():
    return {"message" : "Welcome to users code"}

@app.get("/users")
def get_all_users():
    return users

@app.post("/user")
def add_user(user : User):
    user.id = max([u.id for u in users if u.id is not None], default=0) + 1
    users.append(user)
    return {"message" : "User Added Successfully" , "user" : user}

@app.put("/user/{user_id}")
def update_user(user_id : int , updated_user:User):
    for index , user in enumerate(users):
        if user.id == user_id:
            updated_user.id = user_id
            users[index] = updated_user
            return {"message" : "User Updated Successfully" , "user" : updated_user}
    return {
        "message" : "User Not Found",
        "error" : True
    }

@app.delete("/user/{user_id}")
def delete_user(user_id : int):
    for index , user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return {"message" : "User Deleted Successfully" , "user" : deleted_user}
    return {
        "message" : "User Not Found",
        "error" : True
    }