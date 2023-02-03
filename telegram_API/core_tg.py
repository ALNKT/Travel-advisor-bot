import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage

from settings import BotSettings


bot_token = BotSettings().bot_token.get_secret_value()

logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='w',
                    datefmt=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'),
                    format='%(asctime)s - %(levelname)s - %(message)s')

storage = JSONStorage('JSONStorage.json')
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)
