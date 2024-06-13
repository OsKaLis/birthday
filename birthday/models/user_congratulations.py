from sqlalchemy import Column, ForeignKey, Integer, DateTime, Text

from birthday.core.db import Base
from birthday.core.config import settings


class UserCongratulations(Base):
    author_id = Column(Integer, ForeignKey('user.id'))
    congratulated_id = Column(Integer, ForeignKey('user.id'))
    text_greeting = Column(Text, nullable=False)
    data_greeting = Column(DateTime, default=settings.current_time())
