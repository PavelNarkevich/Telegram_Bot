from aiogram.filters import Filter
from aiogram import Bot, types

from api.middlewares.settings import settings


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        return message.from_user.id == settings.bots.admin_id
