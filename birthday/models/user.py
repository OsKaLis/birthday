from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, String

from birthday.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    patrony = Column(String, nullable=False)
    birthdate = Column(DateTime)
