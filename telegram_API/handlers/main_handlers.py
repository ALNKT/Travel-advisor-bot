from aiogram import types

from database.CRUD import record_user
from telegram_API import keyboards
from telegram_API.core_tg import dp
from telegram_API.texts import greeting_text, help_text


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """
    Приветствие пользователя
    :param message: сообщение
    """
    record_user(username=message.from_user.username, first_name=message.from_user.first_name)
    text_message = greeting_text.format(name=message.from_user.first_name)
    await message.answer(text_message, reply_markup=keyboards.hello_keyboard)  # пользователь выбирает кнопку (Да, Нет)


@dp.callback_query_handler(text=['Да', 'Нет'])
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


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    """
    Выводит справку по возможностям бота
    :param message: сообщение
    """
    await message.answer(help_text)
