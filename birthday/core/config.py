from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    title: str = 'Birthday'
    app_author: str = 'Oskalis'
    path: str
    description: str = 'Описание проекта.'
    database_url: str = 'sqlite+aiosqlite:///./birthday.db'
    secret: str = 'SECRET'
    first_name: str = 'SECRET'
    last_name: str = 'SECRET'
    patrony: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
