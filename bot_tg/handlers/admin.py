from create_bot import dp
from data_base import sqlite_db
from keyboards import kb_admin

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text



ID = 381947893

class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	description = State()
	rating = State()


async def admin(message : types.Message):
	if ID == message.from_user.id:
		await message.answer('держи', reply_markup=kb_admin)
	else:
		await message.reply('ты не Булат(')


	#начало диалога
# @dp.message_handlers(command='Загрузить', state=None)
async def cm_start(message : types.Message):
	if ID == message.from_user.id:
		await FSMAdmin.photo.set()
		await message.reply('Загрузи фото')
	

	#ловим первый ответ и в память
# @dp.message_handlers(context_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply('Введите название')

	#ловим второй ответ
# @dp.message_handlers(state=FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply('Введите описание')



	#ловим третий ответ
# @dp.message_handlers(state=FSMAdmin.description)
async def load_description(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
	await FSMAdmin.next()
	await message.reply('Введите рейтинг')


		#ловим четвертый ответ и записываем в бд
# @dp.message_handlers(state=FSMAdmin.rating)
async def load_rating(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['rating'] = float(message.text)


	await sqlite_db.sql_add_command(state)
	await message.reply('Готово')


	await state.finish()


#отмена
# @dp.message_handlers(state='*', commands='отмена')
# @dp.message_handlers(Text(equals='отмена', ignore_case=True), state='@')
async def cancel_handler(message:types.Message,state:FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply('kk')




def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(admin, commands='admin')
	dp.register_message_handler(cm_start, commands='загрузить', state=None)	
	dp.register_message_handler(cancel_handler, state='*', commands='отмена')
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_description, state=FSMAdmin.description)
	dp.register_message_handler(load_rating, state=FSMAdmin.rating)