from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    token_type: Optional[str] = 'bearer'
    access_token: Optional[str]
    refresh_token: Optional[str]
    expire_token: Optional[datetime]
    expire_refresh_token: Optional[datetime]


class TokenCreate(BaseModel):
    user_name: Optional[str]
    password: Optional[str]


class TokenPayload(BaseModel):
    user_name: Optional[str]
    password: Optional[str]