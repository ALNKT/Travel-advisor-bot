import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage

from settings import BotSettings


bot_token = BotSettings().bot_token.get_secret_value()
# filename='bot.log',
logging.basicConfig(level=logging.INFO, filemode='w',
                    datefmt=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'),
                    format='%(asctime)s - %(levelname)s - %(message)s')

storage = JSONStorage('JSONStorage.json')
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)

# @dp.message_handler(commands=["history"])
# async def cmd_history(message: types.Message):
#     """
#     Выводит список всех записей в базе данных
#     :param message: сообщение
#     """
#     read_data_from_DB = read_data(message.from_user.first_name, 3)
#     for j in read_data_from_DB:
#         await message.answer(text=j, parse_mode=None)

#
# @dp.message_handler(commands=['mylocation'])
# async def cmd_location(message: types.Message):
#     """
#     Обработка команды 'mylocation'
#     :param message: сообщение
#     """
#     await message.reply("Давай определим твоё местоположение.", reply_markup=keyboards.request_geo)
#

# @dp.message_handler()
# async def echo(message: types.Message):
#     # create_data(message.from_user.username, message.from_user.first_name, message.text)
#     await message.answer(message.text)
#     print(message)
