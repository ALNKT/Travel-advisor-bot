import datetime

from database.models import db, Users, RequestsHotels, RequestsRestaurants, RequestsAttractions


def init_db():
    """
    Инициализация базы данных
    """
    db.connect()
    db.create_tables([Users, RequestsHotels, RequestsRestaurants, RequestsAttractions])


def close_db():
    """
    Закрытие базы данных
    :return:
    """
    db.close()


def check_user(first_name: str):
    """
    Проверка наличия пользователя в базе данных
    :param first_name: имя пользователя
    :return: bool
    """
    if Users.select(Users.first_name).where(Users.first_name == first_name):
        return True
    return False


def record_user(username: str, first_name: str):
    """
    Занесение пользователя в базу данных. Предварительно проверяем его наличие в таблице
    :param username: username пользователя
    :param first_name: имя пользователя
    """
    if not check_user(first_name):
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        data_command = Users(date=date, username=username, first_name=first_name)
        data_command.save()


def record_request(first_name, request, table, date=datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")):
    """
    Запись данных в таблицу с запросами пользователя
    :param date: текущая дата
    :param table: таблица, в которую записывать данные
    :param first_name: имя пользователя
    :param request: запрос пользователя
    """
    user_id = next(iter(Users.select(Users.id).where(Users.first_name == first_name)))
    table(date=date, user_id=user_id, request=request).save()


# def read_data(first_name, count=1):
#     """
#     Получение данных из базы
#     :param first_name: имя пользователя
#     :param count: количество записей
#     """
#     data = Data.select().where(Data.first_name == first_name).order_by(Data.id.desc()).limit(count)
#     for i in data:
#         yield i.data

# if __name__ == "__main__":
#     user_id = next(iter(Users.select(Users.id).where(Users.first_name == 'Alex')))
#     print(user_id)
#     Requests(user_id=user_id, request='abc').save()
