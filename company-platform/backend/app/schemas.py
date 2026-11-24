from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=256)
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
class CEOResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email: str
    is_active: bool
class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    slug: str
    display_name: str
    role: str
    department: str
    status: str
    created_at: datetime
    updated_at: datetime
