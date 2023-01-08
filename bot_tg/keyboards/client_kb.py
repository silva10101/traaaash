from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # ReplyKeyboardMarkup



b1 = KeyboardButton('/start')
b2 = KeyboardButton('/привет')
b3 = KeyboardButton('/мя')
b4 = KeyboardButton('/данные')
b5 = KeyboardButton('/admin')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).add(b4).insert(b5)



# KeyboardButton('Поделиться номером', request_contact=True)
# KeyboardButton('Местоположение',request_location=True)
