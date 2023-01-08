from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # ReplyKeyboardMarkup



button_load = KeyboardButton('/загрузить')
button_delete = KeyboardButton('/удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(button_load).add(button_delete)
