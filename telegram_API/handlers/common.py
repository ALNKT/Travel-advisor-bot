from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from database.CRUD import record_user_db, read_data_of_restaurants
from telegram_API import keyboards
from telegram_API.core_tg import dp, bot
from telegram_API.texts import greeting_text, help_text


class SearchRestaurants(StatesGroup):
    waiting_for_category = State()
    waiting_for_count = State()


async def cmd_cancel(message: types.Message, state: FSMContext):
    """
    Отмена команды
    :param message: сообщение
    :param state: статус
    """
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())


async def cmd_start(message: types.Message):
    """
    Приветствие пользователя
    :param message: сообщение
    """
    record_user_db(username=message.from_user.username, first_name=message.from_user.first_name)
    text_message = greeting_text.format(name=message.from_user.first_name)
    await message.answer(text_message, reply_markup=keyboards.hello_keyboard)  # пользователь выбирает кнопку (Да, Нет)


async def processing_button_yes_no(call: types.CallbackQuery):
    """
    Обработка кнопок "Да" и "Нет"
    """
    if call.data == 'yes':
        await call.message.answer(text=f'Отлично, давай я тебе расскажу обо всем...\n{help_text}')
    elif call.data == 'no':
        await call.message.answer(text=f'Отлично, я рад, что ты все знаешь. Тогда жду от тебя команду.')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()


async def cmd_history(message: types.Message, state: FSMContext):
    """
    Выводит историю запросов пользователя
    :param message: сообщение
    :param state: статус
    """
    await message.answer('По результатам каких запросов, вы хотите просмотреть историю?',
                         reply_markup=keyboards.history_keyboard)
    await state.set_state(SearchRestaurants.waiting_for_category.state)


async def processing_history_keyboard(call: types.CallbackQuery, state: FSMContext):
    """
    Обработка кнопок "Просмотреть историю"
    """
    await state.update_data(category=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    if call.data == 'restaurants':
        await call.message.answer(text=f'Сколько результатов вывести?', reply_markup=keyboards.count_keyboard)
        await state.set_state(SearchRestaurants.waiting_for_count.state)
    elif call.data == 'hotels':
        pass
    elif call.data == 'places':
        pass


async def processing_count_keyboard(call: types.CallbackQuery, state: FSMContext):
    """
    Обработка количества результатов
    """
    await state.update_data(count=call.data)
    user_data = await state.get_data()
    await state.finish()
    await call.message.answer(text=f'Подождите, обрабатываю ваш запрос.')
    await call.message.edit_reply_markup(reply_markup=None)
    category, count = user_data['category'], int(user_data['count'])
    if category == 'restaurants':
        results = read_data_of_restaurants(call.from_user.first_name, count)
        for n, i_data in enumerate(results):
            restaurant_data = i_data[0]
            restaurant_coordinates = i_data[1]
            await call.message.answer(text=f'<u><b>Результат №{n + 1}</b></u>\n{restaurant_data}', parse_mode='HTML')
            if restaurant_coordinates is not None:
                await call.message.answer_location(restaurant_coordinates[0], restaurant_coordinates[1])


async def cmd_help(message: types.Message):
    """
    Выводит справку по возможностям бота
    :param message: сообщение
    """
    await message.answer(help_text)


def register_handlers_common(dps: Dispatcher):
    """
    Регистрируем общие обработчики
    :param dps: диспетчер
    """
    dps.register_message_handler(cmd_start, commands="start", state="*")
    dps.register_message_handler(cmd_help, commands="help", state="*")
    dps.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
    dps.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dps.register_message_handler(cmd_history, commands="history", state="*")


def register_callbacks(dps: Dispatcher):
    """
    Регистрация коллбэков
    :param dps: диспетчер
    """
    dps.register_callback_query_handler(processing_button_yes_no, Text(['yes', 'no']), state="*")
    dps.register_callback_query_handler(processing_history_keyboard, Text(['restaurants', 'hotels', 'places']),
                                        state=SearchRestaurants.waiting_for_category)
    dps.register_callback_query_handler(processing_count_keyboard,
                                        Text(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
                                        state=SearchRestaurants.waiting_for_count)


register_handlers_common(dp)
register_callbacks(dp)
