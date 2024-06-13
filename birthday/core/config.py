from datetime import datetime as dt, timedelta as td
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
    birthday_warning: int = 10

    class Config:
        env_file = '.env'

    def current_time(self) -> dt:
        """Узнать текущию дату."""
        return dt.now()

    def the_birthday_is_coming_soon(
            self,
            desired_date: int,
            range_of_days: int = None
    ) -> bool:
        """Проверяет в ходит ли в диапазон запрашиваемый день рождения."""
        current_data = self.current_time()
        if range_of_days is None:
            range_of_days = settings.birthday_warning
        current_time_plus_period = current_data + td(days=range_of_days)

        if current_data <= desired_date <= current_time_plus_period:
            return True
        return False


settings = Settings()
