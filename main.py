from aiogram.types import AllowedUpdates
from aiogram.utils import executor

from database.CRUD import init_db, close_db, read_data
from telegram_API.core import *

init_db()

executor.start_polling(dp, skip_updates=True)
close_db()
