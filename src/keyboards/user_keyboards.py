from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class UserKeyboards:
    @staticmethod
    def main_menu():
        btn_conn = KeyboardButton(text="Получить доступ🚀")
        
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [btn_conn]
            ],
            resize_keyboard=True
        )
        return keyboard
    