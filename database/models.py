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


class Data(BaseModel):
    """
    Таблица для хранения данных о сообщениях пользователя
    """
    date = DateTimeField(null=True)
    username = TextField(null=True)
    first_name = TextField(null=True)
    data = TextField(null=True)
