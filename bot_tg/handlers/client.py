from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove



#@dp.message_handler(commands=['start', 'help'])
async def start_command(message : types.Message):
    try:
        await message.answer('хыыыы', reply_markup=kb_client)
    except:
        await message.reply('Напиши в лс :)')


#@dp.message_handler(commands=['привет'])
async def say_hello_command(message : types.Message):
    await bot.send_message(message.from_user.id, message.from_user.id)


#@dp.message_handler(commands=['мя'])
async def say_mya_command(message : types.Message):
    await message.answer('мя!!!', reply_markup=ReplyKeyboardRemove())


#@dp.message_handler(commands=['данные'])
async def send_data_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(say_hello_command, commands=['привет'])
    dp.register_message_handler(say_mya_command, commands=['мя'])
    dp.register_message_handler(send_data_command, commands=['данные'])