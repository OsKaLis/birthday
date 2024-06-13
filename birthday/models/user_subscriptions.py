from sqlalchemy import Column, ForeignKey, Integer

from birthday.core.db import Base


class UserSubscriptions(Base):
    subscriber_id = Column(Integer, ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
