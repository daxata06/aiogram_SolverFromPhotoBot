from aiogram.types import CallbackQuery, ParseMode
from main import dp, bot
from functions.user_functions.process_answer_function import *
from main import FSM
from keyboards.inline.start_keyboard import *
from keyboards.inline.check_subscribe import *
from handlers.user_handlers import *
from functions.private_functions.check_subscribe import check_sub
from aiogram.types import Message


@dp.callback_query_handler(text="start_using") 
async def get_information(call: CallbackQuery, state: FSM):
      is_syb = await check_sub(user_id=call.message.chat.id)
      if is_syb is True:
        markup = None
        msg = "📸*Сейчас пришли фото.*\n\n__Фото должно быть чётким, в кадре должно быть только то, что тебе нужно решить! Обрежь фото перед отправкой__"
        await FSM.getphotop.set()
      else:
       markup = await checksubscribe()
       msg = '❌Для использования бота небоходимо подписаться на канал'
      await bot.send_message(call.message.chat.id, text=msg, reply_markup=markup, parse_mode='Markdown')


@dp.callback_query_handler(text="how_using")
async def using_tutor_doc(call: CallbackQuery):
   await call.bot.send_document(chat_id=call.message.chat.id, document=open("Публичная оферта.docx", "rb"))


@dp.callback_query_handler(text="check_subscribe")
async def check_s(call: CallbackQuery):
     is_syb = await check_sub(user_id=call.message.chat.id)

     if is_syb is True:
       markup = None
       msg = f"✅*Теперь вы можете пользоваться ботом!*\nПродолжите использование, нажав /start или нажав на кнопку 'Решить'"

     else:
       markup = await checksubscribe()
       msg = '❌*Для использования бота небоходимо подписаться на канал*'
     await bot.send_message(call.message.chat.id, text=msg, reply_markup=markup, parse_mode='Markdown')


@dp.callback_query_handler(text="rassilka")
async def make_rassilka(call: CallbackQuery, state: FSM):
   await  FSM.rassil.set()
   await bot.send_message(call.message.chat.id, 'Напиши текст рассылки')


@dp.message_handler(lambda message: message.text == "Назад")
async def back_to_menu(message: Message):
   if message.text == 'Назад':
      markup = await Start_keyboard(user_id=message.from_user.id)
      msg = '*Главное меню*\n\n🟩Выбор действия:'
      await bot.send_message(message.chat.id, text=msg, reply_markup=markup, parse_mode='Markdown')


