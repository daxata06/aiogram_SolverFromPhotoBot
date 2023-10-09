from main import dp, FSM
from aiogram import executor
from logic import Logic


dp.register_message_handler(Logic.start, commands=['start'], state=None)
#dp.register_message_handler(rass, commands=['rassilka'], state=None)
#dp.register_callback_query_handler(inline_button_handler, lambda c: c.data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)