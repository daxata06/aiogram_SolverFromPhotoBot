from aiogram.types import CallbackQuery
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ContentType, ParseMode
from main import FSM, dp, bot
from functions.private_functions.gpt import *
from functions.private_functions.text import *
from keyboards.default.back_keyboard import *

@dp.message_handler(content_types=[ContentType.PHOTO, ContentType.TEXT],state=FSM.getphotop)
async def process_answer(message: Message, state: FSM,):
    try:
     photo = message.photo[-1]
     markup = await backkeyb()
     await bot.send_message(message.chat.id, text=  await getphoto(photo, content=''), reply_markup=markup)
     await state.finish()
    except Exception as e:
      print(e)
      await bot.send_message(message.chat.id, text='❗Отправьте фото!')