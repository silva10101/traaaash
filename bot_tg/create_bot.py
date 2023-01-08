from aiogram import Bot
from aiogram.dispatcher import Dispatcher 
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from os import getenv

storage = MemoryStorage()

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
