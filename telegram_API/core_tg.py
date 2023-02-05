from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage

from settings import BotSettings, logger

bot_token = BotSettings().bot_token.get_secret_value()

logger.info('STARTING BOT'.center(91, '='))

storage = JSONStorage('JSONStorage.json')
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)
