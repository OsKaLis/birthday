from fastapi import FastAPI

from birthday.api.routers import main_router
from birthday.core import settings, create_first_superuser

app = FastAPI(title=settings.title)
app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
