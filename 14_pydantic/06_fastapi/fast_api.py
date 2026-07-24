from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name : str = "FastAPI"
    admin_email : str = "admin@fastapi.com"

def get_settings() -> Settings:
    return Settings()
    
@app.post("/signup")
def signup(user:UserSignup):
    return {"message" : f"User {user.username} has been created"}

@app.get("/settings")
def get_settings_endpoint(settings : Settings = Depends(get_settings)):
    return settings