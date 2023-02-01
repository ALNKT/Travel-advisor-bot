import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import BotSettings


bot_token = BotSettings().bot_token.get_secret_value()
# filename='bot.log',
logging.basicConfig(level=logging.INFO, filemode='w',
                    datefmt=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'),
                    format='%(asctime)s - %(levelname)s - %(message)s')

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())




# @dp.message_handler(commands=["history"])
# async def cmd_history(message: types.Message):
#     """
#     Выводит список всех записей в базе данных
#     :param message: сообщение
#     """
#     read_data_from_DB = read_data(message.from_user.first_name, 3)
#     for i in read_data_from_DB:
#         await message.answer(text=i, parse_mode=None)

#
# @dp.message_handler(commands=['mylocation'])
# async def cmd_location(message: types.Message):
#     """
#     Обработка команды 'mylocation'
#     :param message: сообщение
#     """
#     await message.reply("Давай определим твоё местоположение.", reply_markup=keyboards.request_geo)
#
#
# @dp.message_handler(content_types=ContentTypes.LOCATION)
# async def processing_user_location(message: types.Message):
#     """
#     Получаем данные геолокации
#     :param message: геолокация
#     """
#     await message.reply(text=None, reply_markup=keyboards.ReplyKeyboardRemove())
#     coordinates = (message.location.latitude, message.location.longitude)
#     return coordinates


# @dp.message_handler(content_types=ContentTypes.CONTACT)
# async def user_location(message: types.Message):
#     await message.answer(f'Телефон: {message.contact.phone_number}', reply_markup=keyboards.ReplyKeyboardRemove())
#     print(f'Телефон: {message.contact.phone_number}')


# @dp.message_handler()
# async def echo(message: types.Message):
#     # create_data(message.from_user.username, message.from_user.first_name, message.text)
#     await message.answer(message.text)
#     print(message)

# @dp.message_handler(commands='1')
# async def echo(message: types.Message):
#     with open('restaurants.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         photo = data['data'][0]['photo']['images']['medium']['url']
#         name = data['data'][0]['name']
#         distance = data['data'][0]['distance_string']
#         phone = data['data'][0]['phone']
#         address = data['data'][0]['address']
#     await bot.send_photo(chat_id=message.chat.id, photo=photo)
#     await message.answer(text=f'Название ресторана: {name}\n'
#                               f'Адрес: {address}\n'
#                               f'Телефон: {phone}\n'
#                               f'Удалённость: {distance}\n')

    # await message.answer(res, parse_mode='HTML')
