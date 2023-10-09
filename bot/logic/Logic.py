from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ContentType, ParseMode
from main import FSM, bot
import asyncio
import threading
from keyboards.inline.start_keyboard import *
from keyboards.inline.check_subscribe import *
from handlers.user_handlers import *
from functions.private_functions.check_subscribe import check_sub


async def start(message: Message, state: FSM):
      is_syb = await check_sub(user_id=message.from_user.id)
      if is_syb is True:
       markup = await Start_keyboard(user_id=message.from_user.id)
       msg = f"👋*Привет!\nЭто бот, с помощью которого ты можешь отсканировать текст и передать его в CHATGpt*\n\nО__бязаательно почитай как пользоваться ботом по кнопке ниже, так как это, поверь, очень важно!__\n\nБот работтает в тестовом режиме и проверяется заинтересованность аудитории, если все будет хорошо и заинтересованность будет, бот будет работать и дальше!\n\nАвтор проекта - @Sofreake"
      else:
       markup = await checksubscribe()
       msg = 'Для использования бота небоходимо подписаться на канал'
      await bot.send_message(message.chat.id, text=msg, reply_markup=markup, parse_mode='Markdown')


@dp.message_handler(state=FSM.rassil)
async def send_message_to_all(message: Message, state: FSM):
  await state.finish()
  with open('users.txt', 'r') as file:
     for line in file:
        try:
         await bot.send_message(chat_id=line, text=message.text)
        except:
            continue


