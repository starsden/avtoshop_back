from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class AuthLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=255)


class AuthUserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str


class AuthLoginResponse(BaseModel):
    user: AuthUserResponse
    token: str


class SessionInfo(BaseModel):
    id: str
    expires_at: datetime
