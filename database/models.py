from peewee import *
import os

path = os.path.abspath('database/travel_advisor.db')

db = SqliteDatabase(path)


class BaseModel(Model):
    """
    Базовая модель
    """
    class Meta:
        database = db


class Users(BaseModel):
    """
    Таблица для хранения данных о пользователях и их командах

    Attributes:
        date (datetime): дата первого запроса
        username (string): username пользователя
        first_name (string): имя пользователя
    """
    date = DateTimeField(null=True)
    username = CharField(null=True)
    first_name = CharField(null=True)


# class Requests(BaseModel):
#     """
#     Таблица для хранения данных о введенных командах пользователя
#
#     Attributes:
#         user_id (int): id пользователя
#         request (string): запрос пользователя
#     """
#     user_id = IntegerField(null=True)
#     request = TextField(null=True)


class RequestsHotels(BaseModel):
    """
    Таблица для хранения запросов по отелям

    Attributes:
        user_id (int): id пользователя
        request (string): запрос пользователя
        answer (string): ответ от сервера
    """
    user_id = IntegerField(null=True)
    request = TextField(null=True)
    answer = TextField(null=True)


class RequestsRestaurants(BaseModel):
    """
    Таблица для хранения запросов по ресторанам

    Attributes:
        user_id (int): id пользователя
        request (string): запрос пользователя
        answer (string): ответ от сервера
    """
    user_id = IntegerField(null=True)
    request = TextField(null=True)


class RequestsAttractions(BaseModel):
    """
    Таблица для хранения запросов по достопримечательностям

    Attributes:
        user_id (int): id пользователя
        request (string): запрос пользователя
        answer (string): ответ от сервера
    """
    user_id = IntegerField(null=True)
    request = TextField(null=True)
    answer = TextField(null=True)
