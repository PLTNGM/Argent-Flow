from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.database.model import SponsorSubOrm

class UserKeyboards:
    @staticmethod
    def main_menu():
        btn_conn = InlineKeyboardButton(text="Получить доступ🚀", callback_data="get_access")
        
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [btn_conn]
            ]
        )
        return keyboard
    
    @staticmethod
    def sponsor_buttons(sponsors: list[SponsorSubOrm]):
        builder = InlineKeyboardBuilder()
        
        for sponsor in sponsors:
            btn_text = sponsor.name if sponsor.name else "Подписаться на канал"
            
            builder.row(InlineKeyboardButton(
                text=btn_text, 
                url=sponsor.url
            ))
        
        builder.row(InlineKeyboardButton(
            text="Я подписался ✅", 
            callback_data="check_subs"
        ))
        
        builder.adjust(1)
        
        return builder.as_markup()
    