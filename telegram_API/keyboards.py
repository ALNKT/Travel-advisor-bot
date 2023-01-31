from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True))\
    .add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))

button_1 = KeyboardButton('Это я')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_1)
