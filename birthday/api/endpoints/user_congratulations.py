from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.core import get_async_sessino, current_user
from birthday.api.validators import check_user_exists
from birthday.models.user import User
from birthday.crud import user_congratulations_crud
from birthday.schemas.user_congratulations import (
    UserCongratulationsCreate, UserCongratulationssShow
)

router = APIRouter()


@router.get(
    '/',
    response_model=list[UserCongratulationssShow],
    dependencies=[Depends(current_user)],
    tags=['Просмотреть мои поздравиления.']
)
async def get_congratulations_all_my(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_sessino),
):
    """Показать последние мои поздравления."""
    return await user_congratulations_crud.get_all_congratulations_user(
        user.id, session
    )


@router.post(
    '/{user_id}',
    response_model=UserCongratulationsCreate,
    dependencies=[Depends(current_user)],
    tags=['Отправить поздравление пользователю.']
)
async def create_congratulations_user(
    user_id: int,
    text_greeting: str,
    session: AsyncSession = Depends(get_async_sessino),
    author_id: User = Depends(current_user),
):
    """Отправляю поздравление пользователю."""
    obj_user = await check_user_exists(user_id, session)
    return await user_congratulations_crud.create(
        author_id, obj_user, text_greeting, session
    )
