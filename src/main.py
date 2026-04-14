import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.config import settings
from src.handlers.user_handlers import router as user_router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token= settings.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    print("")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот не стартанул")