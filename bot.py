import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- НАСТРОЙКИ ---
# Токен лучше не хранить в коде: задай его как переменную окружения BOT_TOKEN.
# Для быстрого локального теста можно временно вписать строкой ниже.
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER")

# Ссылка на твой мини-апп после публикации (GitHub Pages и т.п.), обязательно https
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://ТВОЙ_НИК.github.io/stardust-app/")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="✨ Играть в Звёздную пыль",
                web_app=WebAppInfo(url=WEBAPP_URL),
            )
        ]]
    )
    await message.answer(
        "Привет! Тапай по звезде, собирай космическую пыль и качай апгрейды 🌌",
        reply_markup=kb,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
