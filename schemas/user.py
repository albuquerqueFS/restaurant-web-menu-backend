from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        from_attributes = True

class UserRead(BaseModel):
    username: str
    email: str
    password: str

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
