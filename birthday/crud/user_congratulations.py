from sqlalchemy.ext.asyncio import AsyncSession

from birthday.crud.base import CRUDBase
from birthday.core import settings
from birthday.models import UserCongratulations, User


class CRUDUserCongratulations(CRUDBase):

    async def create(
        self,
        author_id: User,
        obj_user: User,
        text_greeting: str,
        session: AsyncSession,
    ) -> UserCongratulations:
        """Поздравить пользавателя."""
        db_obj = self.model(
            author_id=author_id.id,
            congratulated_id=obj_user.id,
            text_greeting=text_greeting,
            data_greeting=settings.current_time()
        )
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


user_congratulations_crud = CRUDUserCongratulations(UserCongratulations)
