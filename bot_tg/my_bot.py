from create_bot import dp  
from data_base import sqlite_db

from aiogram.utils import executor



async def on_startup(_):
    sqlite_db.sql_start()
    print('Бот запущен')


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)