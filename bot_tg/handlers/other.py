from create_bot import dp

from aiogram import types, Dispatcher



#@dp.message_handler()
async def echo_send(message: types.Message):
    await message.reply('я так не умею')
    #await message.delete()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
