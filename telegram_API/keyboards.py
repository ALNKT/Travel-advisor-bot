from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

request_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True))\
    .add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))

hello_button_yes = InlineKeyboardButton('Да, хочу узнать!', callback_data='Да')
hello_button_no = InlineKeyboardButton('Нет, я всё знаю!', callback_data='Нет')
hello_keyboard = InlineKeyboardMarkup().row(hello_button_yes, hello_button_no)
