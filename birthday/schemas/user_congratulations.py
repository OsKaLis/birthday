# from datetime import datetime
# from typing import Optional

from pydantic import BaseModel


class UserCongratulationsBase(BaseModel):
    text_greeting: str


class UserCongratulationsCreate(UserCongratulationsBase):
    congratulated_id: int

    class Config:
        orm_mode = True
