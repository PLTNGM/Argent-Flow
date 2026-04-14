from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.database.dao.user_dao import UserDao
from src.utils.texts import BotTexts
from src.keyboards.user_keyboards import UserKeyboards

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await UserDao.register_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )
    await message.answer(
        text=BotTexts.start_message(message.from_user.first_name),
        reply_markup=UserKeyboards.main_menu()
    )