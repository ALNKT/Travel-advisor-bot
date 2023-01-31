import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentTypes

from database.CRUD import read_data
from settings import BotSettings
from telegram_API import keyboards
from telegram_API.texts import greeting_text, help_text

bot_token = BotSettings().bot_token.get_secret_value()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """
    Приветствие пользователя
    :param message: сообщение
    """
    text_message = greeting_text.format(name=message.from_user.first_name)
    await message.answer(text_message, reply_markup=keyboards.hello_keyboard)  # пользователь выбирает кнопку (Да, Нет)


@dp.callback_query_handler(text=['Да', 'Нет'])
async def send_random_value(call: types.CallbackQuery):
    """
    Обработка кнопок "Да" и "Нет"
    """
    await call.message.edit_reply_markup(reply_markup=None)
    if call.data == 'Да':
        await call.message.answer(text=f'Отлично, давай я тебе расскажу обо всем...\n{help_text}')
    elif call.data == 'Нет':
        await call.message.answer(text=f'Отлично, я рад, что ты все знаешь. Тогда жду от тебя команду.')


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    """
    Выводит справку по возможностям бота
    :param message: сообщение
    """
    await message.answer(help_text)


@dp.message_handler(commands=["history"])
async def cmd_history(message: types.Message):
    """
    Выводит список всех записей в базе данных
    :param message: сообщение
    """
    read_data_from_DB = read_data(message.from_user.first_name, 3)
    for i in read_data_from_DB:
        await message.answer(text=i, parse_mode=None)


@dp.message_handler(commands=['mylocation'])
async def process_location_command(message: types.Message):
    """
    Обработка команды 'mylocation'
    :param message: сообщение
    """
    await message.reply("Запрашиваем геолокацию", reply_markup=keyboards.request_geo)


@dp.message_handler(content_types=ContentTypes.LOCATION)
async def user_location(message: types.Message):
    """
    Получаем данные геолокации
    :param message: геолокация
    """
    await message.answer(f'Широта: {message.location.latitude}\nДолгота: {message.location.longitude}',
                         reply_markup=keyboards.ReplyKeyboardRemove())
    print(f'Широта: {message.location.latitude}\nДолгота: {message.location.longitude}')


# @dp.message_handler(content_types=ContentTypes.CONTACT)
# async def user_location(message: types.Message):
#     await message.answer(f'Телефон: {message.contact.phone_number}', reply_markup=keyboards.ReplyKeyboardRemove())
#     print(f'Телефон: {message.contact.phone_number}')


# @dp.message_handler()
# async def echo(message: types.Message):
#     # create_data(message.from_user.username, message.from_user.first_name, message.text)
#     await message.answer(message.text)
#     print(message)
