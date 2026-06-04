from pydantic import BaseModel, EmailStr, ConfigDict

from app.enums.enums import UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    model_config = ConfigDict(
        from_attributes=True
    )