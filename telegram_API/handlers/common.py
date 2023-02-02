from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from database.CRUD import record_user
from telegram_API import keyboards
from telegram_API.core_tg import dp
from telegram_API.texts import greeting_text, help_text


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())


async def cmd_start(message: types.Message):
    """
    Приветствие пользователя
    :param message: сообщение
    """
    record_user(username=message.from_user.username, first_name=message.from_user.first_name)
    text_message = greeting_text.format(name=message.from_user.first_name)
    await message.answer(text_message, reply_markup=keyboards.hello_keyboard)  # пользователь выбирает кнопку (Да, Нет)


async def processing_button_yes_no(call: types.CallbackQuery):
    """
    Обработка кнопок "Да" и "Нет"
    """
    await call.message.edit_reply_markup(reply_markup=None)
    if call.data == 'Да':
        await call.message.answer(text=f'Отлично, давай я тебе расскажу обо всем...\n{help_text}')
    elif call.data == 'Нет':
        await call.message.answer(text=f'Отлично, я рад, что ты все знаешь. Тогда жду от тебя команду.')
    await call.answer()


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


def register_callbacks(dps: Dispatcher):
    """
    Регистрация коллбэков
    :param dps: диспетчер
    """
    dps.register_callback_query_handler(processing_button_yes_no, Text(['Да', 'Нет']), state="*")


register_handlers_common(dp)
register_callbacks(dp)
