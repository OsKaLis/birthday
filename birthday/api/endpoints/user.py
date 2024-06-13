from typing import Optional
from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.core import (current_superuser,
                           current_user, get_async_sessino)
from birthday.core.user import auth_backend, fastapi_users
from birthday.schemas.user import (
    UserCreate, UserRead, UserUpdate
)
from birthday.models import User
from birthday.core import settings
from birthday.crud import user_subscriptions_crud

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['Авторизация и регистрация'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['Авторизация и регистрация'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['Работа с Пользователями'],
    dependencies=[Depends(current_superuser)],
)


@router.get(
    '/users/all',
    response_model=list[UserRead],
    dependencies=[Depends(current_user)],
    response_model_exclude={
        'is_active', 'is_superuser', 'is_verified', 'patrony'},
    tags=['Поиск пользователя.'],
)
async def get_all_user(
    session: AsyncSession = Depends(get_async_sessino),
) -> list[UserRead]:
    """Показать всех пользователей для поиска."""
    all_user = await session.execute(
        select(User)
    )
    return all_user.scalars().all()


@router.get(
    '/users/сongratulations/soon',
    response_model=list[UserRead],
    dependencies=[Depends(current_user)],
    response_model_exclude={
        'is_active', 'is_superuser', 'is_verified', 'patrony'},
    tags=['Узнать когда у пользователя День рождения.'],
)
async def get_сongratulations_soon_user(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_sessino),
    days: Optional[int] = None,
) -> list[UserRead]:
    """Узнать укого скоро день рождения."""
    my_pod_uz = await user_subscriptions_crud.get_all_subscriptions_user(
        user.id, session
    )
    satisfying_birthday: list = []
    for user_obj in my_pod_uz:
        user_obj.birthdate = user_obj.birthdate.replace(
            year=settings.current_time().year
        )
        if settings.the_birthday_is_coming_soon(user_obj.birthdate, days):
            print(f'{user_obj.id} - {user_obj.birthdate.day}')
            satisfying_birthday.append(user_obj.id)
    soon_сongratulations_user = await session.execute(
        select(User).filter(User.id.in_(satisfying_birthday))
    )
    return soon_сongratulations_user.scalars().all()


@router.delete(
    '/users/{id}',
    tags=['Работа с Пользователями'],
    deprecated=True
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail='Удаление пользователей запрещено!'
    )
