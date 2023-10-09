from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def checksubscribe():
    markup = InlineKeyboardMarkup(row_width=1)
    subscribe = InlineKeyboardButton(
        text=("✔️Подписался"), callback_data="check_subscribe"
    )
    channel = InlineKeyboardButton(text="Канал", url="https://t.me/daxtopbotsstudio")
    markup.add(subscribe, channel)
    return markup