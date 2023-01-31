from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

# создаем клавиатуру для отправки геопозиции
request_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))


# создаем клавиатуру с двумя кнопками для приветственного сообщения
hello_button_yes = InlineKeyboardButton('Да, хочу узнать!', callback_data='Да')
hello_button_no = InlineKeyboardButton('Нет, я всё знаю!', callback_data='Нет')
hello_keyboard = InlineKeyboardMarkup().row(hello_button_yes, hello_button_no)
