from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from birthday.crud.base import CRUDBase
from birthday.models import UserSubscriptions, User


class CRUDUserSubscriptions(CRUDBase):

    async def create(
        self,
        user: User,
        obj_in: User,
        session: AsyncSession,
    ) -> UserSubscriptions:
        """Подписаться на пользователя."""
        db_obj = self.model(subscriber_id=user.id, user_id=obj_in.id)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def subscription_search(
        self,
        subscriber: int,
        user_id: int,
        session: AsyncSession,
    ) -> UserSubscriptions:
        """Поиск подписки на определёного пользователя."""
        subscriptions_user = await session.execute(
            select(UserSubscriptions).where(
                UserSubscriptions.subscriber_id == subscriber,
                UserSubscriptions.user_id == user_id,
            )
        )
        return subscriptions_user.scalars().first()

    async def get_all_subscriptions_user(
        self,
        user_id: int,
        session: AsyncSession,
    ) -> list[User]:
        """Показать все подписки дни рождения
        на которые подписан пользователь."""
        all_subscriptions_user = await session.execute(
            select(UserSubscriptions.user_id).where(
                UserSubscriptions.subscriber_id == user_id,
            )
        )
        my_user_id = all_subscriptions_user.scalars().all()
        my_subscriptions_user = await session.execute(
            select(User).filter(User.id.in_(my_user_id))
        )
        return my_subscriptions_user.scalars().all()


user_subscriptions_crud = CRUDUserSubscriptions(UserSubscriptions)
