from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.core import current_superuser, current_user, get_async_sessino
from birthday.core.user import auth_backend, fastapi_users
from birthday.schemas.user import (
    UserCreate, UserRead, UserUpdate
)
from birthday.models import User

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
    tags=['Всё что нужно для поздравления.'],
)
async def get_all_user(
    session: AsyncSession = Depends(get_async_sessino),
) -> list[UserRead]:
    """Показать всех пользователей для поиска."""
    all_user = await session.execute(
        select(User)
    )
    return all_user.scalars().all()

# 5) Поиск пользователя

# 1) эндпоит о ближайших днях рождениях

# 3) отправить поздравление пользователю

# 4) Просмотр кто меня поздравил


@router.delete(
    '/users/{id}',
    tags=['Работа с Пользователями'],
    deprecated=True
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail="Удаление пользователей запрещено!"
    )
