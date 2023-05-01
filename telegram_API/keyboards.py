from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

hello_button_yes = InlineKeyboardButton('Да, хочу узнать!', callback_data='yes')
hello_button_no = InlineKeyboardButton('Нет, я всё знаю!', callback_data='no')
hello_keyboard = InlineKeyboardMarkup().row(hello_button_yes, hello_button_no)

request_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True))

button_restaurants = InlineKeyboardButton('Рестораны.', callback_data='restaurants')
button_hotels = InlineKeyboardButton('Отели.', callback_data='hotels')
button_places = InlineKeyboardButton('Достопримечательности.', callback_data='places')
history_keyboard = InlineKeyboardMarkup(row_width=1).add(button_hotels, button_restaurants, button_places)

lst_buttons = [InlineKeyboardButton('1', callback_data='1'), InlineKeyboardButton('2', callback_data='2'),
               InlineKeyboardButton('3', callback_data='3'), InlineKeyboardButton('4', callback_data='4'),
               InlineKeyboardButton('5', callback_data='5'), InlineKeyboardButton('6', callback_data='6'),
               InlineKeyboardButton('7', callback_data='7'), InlineKeyboardButton('8', callback_data='8'),
               InlineKeyboardButton('9', callback_data='9'), InlineKeyboardButton('10', callback_data='10')
               ]
count_keyboard = InlineKeyboardMarkup(row_width=5)
count_keyboard.add(*lst_buttons)


nearest_restaurants = KeyboardButton('Хочу найти ближайшие ко мне рестораны.')
specific_restaurants = KeyboardButton('Хочу найти рестораны в конкретном городе.')
restaurants_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(nearest_restaurants, specific_restaurants)

confirm_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton('Да, всё верно.'), KeyboardButton('Отмена'))


nearest_places = InlineKeyboardButton('Хочу найти ближайшие места.', callback_data='nearest_places')
specific_places = InlineKeyboardButton('Хочу найти места в конкретном городе.',
                                       callback_data='specific_places')
places_keyboard = InlineKeyboardMarkup(row_width=1).\
    add(nearest_places, specific_places)


button_yes = InlineKeyboardButton('Да, все верно.', callback_data='confirm')
button_no = InlineKeyboardButton('Отмена.', callback_data='cancel')
yes_no_keyboard = InlineKeyboardMarkup(row_width=2).add(button_yes, button_no)


nearest_hotels = InlineKeyboardButton('Хочу найти ближайшие отели.', callback_data='nearest_hotels')
specific_hotels = InlineKeyboardButton('Хочу найти отели в конкретном городе.',
                                       callback_data='specific_hotels')
hotels_keyboard = InlineKeyboardMarkup(row_width=1).\
    add(nearest_hotels, specific_hotels)

button_yes = InlineKeyboardButton('Да, все верно.', callback_data='confirm_hotels')
button_no = InlineKeyboardButton('Отмена.', callback_data='cancel')
yes_no_keyboard_hotels = InlineKeyboardMarkup(row_width=2).add(button_yes, button_no)

calendar_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
calendar_keyboard.row('Открыть календарь.')

button_price_range = InlineKeyboardButton('Найти отели по диапазону цен.', callback_data='price_range')
button_min_price = InlineKeyboardButton('Найти отели по минимальной цене.', callback_data='min_price')
button_max_price = InlineKeyboardButton('Найти отели по максимальной цене.', callback_data='max_price')
keyboard_hotels_price = InlineKeyboardMarkup(row_width=1).add(button_price_range, button_min_price, button_max_price)
