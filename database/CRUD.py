import datetime

from database.models import db, Data


def init_db():
    """
    Инициализация базы данных
    """
    db.connect()
    db.create_tables([Data])


def close_db():
    """
    Закрытие базы данных
    :return:
    """
    db.close()


def create_data(username, first_name, data):
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    data = Data(date=date, username=username, first_name=first_name, data=data)
    data.save()


def read_data(first_name, count=1):
    data = Data.select().where(Data.first_name == first_name).order_by(Data.id.desc()).limit(count)
    for i in data:
        yield i.data


if __name__ == "__main__":
    read_data(first_name='Alex', count=3)
