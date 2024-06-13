import datetime
import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from birthday.core import (
    settings, get_async_sessino, get_user_db, get_user_manager
)
from birthday.schemas.user import UserCreate

get_async_session_context = contextlib.asynccontextmanager(get_async_sessino)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    first_name: str, last_name: str, patrony: str,
    email: EmailStr, password: str, is_superuser: bool = False
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    await user_manager.create(
                        UserCreate(
                            first_name=first_name,
                            last_name=last_name,
                            patrony=patrony,
                            birthdate=datetime.datetime.now(),
                            email=email,
                            password=password,
                            is_superuser=is_superuser
                        )
                    )
    except UserAlreadyExists:
        pass


async def create_first_superuser():
    if (settings.first_superuser_email is not None and
            settings.first_superuser_password is not None):
        await create_user(
            first_name=settings.first_name,
            last_name=settings.last_name,
            patrony=settings.patrony,
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            is_superuser=True,
        )
