import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    patrony: str
    birthdate: datetime.date


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    patrony: str
    birthdate: datetime.date


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
    patrony: Optional[str]
    birthdate: Optional[datetime.date]
