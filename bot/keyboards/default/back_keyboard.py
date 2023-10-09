from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def backkeyb():
    markup = ReplyKeyboardMarkup()
    back_button = KeyboardButton("Назад")
    markup.add(back_button)  
    return markup
