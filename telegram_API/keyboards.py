from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

# создаем клавиатуру для отправки геопозиции
request_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))

# создаем клавиатуру с двумя кнопками для приветственного сообщения
hello_button_yes = InlineKeyboardButton('Да, хочу узнать!', callback_data='Да', one_time_keyboard=True)
hello_button_no = InlineKeyboardButton('Нет, я всё знаю!', callback_data='Нет', one_time_keyboard=True)
hello_keyboard = InlineKeyboardMarkup().row(hello_button_yes, hello_button_no)

# # клавиатура для ответа на поиск ресторанов (поблизости или в конкретном городе)
# nearest_restaurants = InlineKeyboardButton('Хочу найти ближайшие ко мне рестораны.', callback_data='поблизости',
#                                            one_time_keyboard=True)
# specific_restaurants = InlineKeyboardButton('Хочу найти рестораны в конкретном городе.', callback_data='город',
#                                             one_time_keyboard=True)
# restaurants_keyboard = InlineKeyboardMarkup().add(nearest_restaurants).add(specific_restaurants)

# # клавиатура для ответа на поиск отелей (поблизости или в конкретном городе)
# nearest_hotels = InlineKeyboardButton('Хочу найти ближайшие отели.', callback_data='поблизости', one_time_keyboard=True)
# specific_city = InlineKeyboardButton('Хочу найти отели конкретного города.', callback_data='город', one_time_keyboard=True)
# hotels_keyboard = InlineKeyboardMarkup().add(nearest_hotels).add(specific_city)


# клавиатура для ответа на поиск ресторанов (поблизости или в конкретном городе)
nearest_restaurants = KeyboardButton('Хочу найти ближайшие ко мне рестораны.')
specific_restaurants = KeyboardButton('Хочу найти рестораны в конкретном городе.')
restaurants_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(nearest_restaurants, specific_restaurants)
