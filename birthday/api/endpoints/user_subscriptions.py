from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.core import (
    get_async_sessino, current_user
)
from birthday.api.validators import (
    check_user_exists,
)
from birthday.models.user import User
from birthday.crud import user_subscriptions_crud
from birthday.schemas.user_subscriptions import (
    UserSubscriptionsBaseShow, UserSubscriptionsBaseList
)

router = APIRouter()


@router.get(
    '/my',
    response_model=list[UserSubscriptionsBaseList],
    dependencies=[Depends(current_user)],
)
async def get_subscriptions_user_all(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_sessino),
):
    """Подписки текущего пользователя."""
    print('gigiugiugiugiug')
    return await user_subscriptions_crud.get_all_subscriptions_user(
        user.id, session
    )


@router.get(
    '/{user_id}',
    response_model=UserSubscriptionsBaseShow,
    dependencies=[Depends(current_user)],
)
async def get_subscriptions_user(
    user_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_sessino),
):
    """Юзер подписывается на другова."""
    obj_user = await check_user_exists(user_id, session)
    return await user_subscriptions_crud.create(
        user, obj_user, session
    )