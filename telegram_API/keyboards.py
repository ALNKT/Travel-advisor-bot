from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

# создаем клавиатуру с двумя кнопками для приветственного сообщения
hello_button_yes = InlineKeyboardButton('Да, хочу узнать!', callback_data='Да', one_time_keyboard=True)
hello_button_no = InlineKeyboardButton('Нет, я всё знаю!', callback_data='Нет', one_time_keyboard=True)
hello_keyboard = InlineKeyboardMarkup().row(hello_button_yes, hello_button_no)


# создаем клавиатуру для отправки геопозиции
request_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))


# КЛАВИАТУРЫ ПО РЕСТОРАНАМ
# клавиатура для ответа на поиск ресторанов (поблизости или в конкретном городе)
nearest_restaurants = KeyboardButton('Хочу найти ближайшие ко мне рестораны.')
specific_restaurants = KeyboardButton('Хочу найти рестораны в конкретном городе.')
restaurants_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(nearest_restaurants, specific_restaurants)

# клавиатура подтверждения запроса на поиск ресторанов
confirm_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Да, всё верно.'), KeyboardButton('Отмена'))
