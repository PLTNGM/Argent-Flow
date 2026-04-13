import asyncio
import logging
from aiogram import Bot, dispatcher
from src.config import settings

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token= settings.BOT_TOKEN.get_secret_value())
    dp = dispatcher()



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот не стартанул")