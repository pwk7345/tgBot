import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os

from app.handlers import router
from app.database.models import async_main


async def main():
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("Токен бота не найден. Убедитесь, что он указан в .env файле как BOT_TOKEN.")

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)

    try:
        await async_main()

        print("Бот запущен. Ожидание сообщений...")
        await dp.start_polling(bot)

    finally:
        await bot.close()
        print("Бот завершил работу.")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен пользователем.")
