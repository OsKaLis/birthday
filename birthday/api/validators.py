from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.models import User


async def check_user_exists(
    user_id: int,
    session: AsyncSession,
):
    """Проверка что пользователь есть в базе."""
    obj_user = await session.execute(
        select(User).where(
            User.id == user_id,
        )
    )
    obj_user = obj_user.scalars().first()
    if obj_user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Юзер не найдена!'
        )
    return obj_user
