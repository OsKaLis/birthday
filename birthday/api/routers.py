from fastapi import APIRouter

from birthday.api.endpoints import (
    user_subscriptions_router, user_router
)

main_router = APIRouter()
main_router.include_router(
    user_subscriptions_router,
    prefix='/subscription',
    tags=['Подписаться']
)
main_router.include_router(user_router)
