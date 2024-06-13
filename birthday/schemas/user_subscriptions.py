from pydantic import BaseModel, Field


class UserSubscriptionsBase(BaseModel):
    user_id: int = Field(..., gt=0)


class UserSubscriptionsBaseShow(UserSubscriptionsBase):
    id: int
    subscriber_id: int = Field(..., gt=0)

    class Config:
        orm_mode = True


class UserSubscriptionsBaseList(UserSubscriptionsBase):

    class Config:
        orm_mode = True
