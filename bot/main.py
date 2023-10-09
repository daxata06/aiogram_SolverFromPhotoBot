from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM(StatesGroup):
    getphotop = State()
    rassil = State()

token='your token'
storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
