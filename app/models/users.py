from beanie import Document
from datetime import datetime
from pydantic import Field, EmailStr

class User(Document):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., unique=True)
    salt: str
    passwordHash: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    profile_url: str = Field(...)

    class Settings:
        name = "users"  
        indexes = [
            "email",  
        ]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "salt": "random_salt_value",
                "passwordHash": "hashed_password_here",
                "is_active": True
            }
        }
