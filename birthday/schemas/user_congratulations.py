from pydantic import BaseModel


class UserCongratulationsBase(BaseModel):
    text_greeting: str


class UserCongratulationssShow(UserCongratulationsBase):
    author_id: int

    class Config:
        orm_mode = True


class UserCongratulationsCreate(UserCongratulationsBase):
    congratulated_id: int

    class Config:
        orm_mode = True
