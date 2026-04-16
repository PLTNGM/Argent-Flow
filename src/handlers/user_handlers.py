from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from src.database.dao.user_dao import UserDao
from src.database.dao.sponsor_dao import SponsorDaoOrm
from src.utils.texts import BotTexts
from src.keyboards.user_keyboards import UserKeyboards

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await UserDao.register_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.first_name
    )
    await message.answer(
        text=BotTexts.start_message(message.from_user.first_name),
        reply_markup=UserKeyboards.main_menu()
    )

@router.callback_query(F.data == "get_access")
async def callback_get_access(callback: CallbackQuery):
    await callback.answer()



    await callback.message.edit_text(
        text=BotTexts.subs_notif_message(),
        reply_markup = UserKeyboards.sponsor_buttons()
    )

@router.callback_query(F.data == "check_subs")
async def check_subscription(callback: CallbackQuery, bot: Bot):
    sponsors = await SponsorDaoOrm.select_all_users()
    
    for sponsor in sponsors:
        member = await bot.get_chat_member(chat_id=sponsor.channel_id, user_id=callback.from_user.id)
        if member.status in ["left", "kicked"]:
            await callback.answer(f"Ты не подписан на {sponsor.name}!", show_alert=True)
            return
    
    await callback.message.edit_text("Красава! Доступ открыт. Держи ссылку...")