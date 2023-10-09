from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import admins_list

async def Start_keyboard(user_id: int):
    markup = InlineKeyboardMarkup(row_width=1)
    start = InlineKeyboardButton(
        text=("🟢Начать использование бота"), callback_data="start_using"
    )
    info = InlineKeyboardButton(
        text=("❓Как пользоваться ботом?"), callback_data="how_using"
    )

    for ids in admins_list.list_admins:
        if ids==user_id:
         rassil = InlineKeyboardButton(
         text=("Сделать рассылку"), callback_data="rassilka"
    )
         markup.add(rassil)
    markup.add(start, info)
    return markup