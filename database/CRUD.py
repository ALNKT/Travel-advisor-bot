import datetime
import json

from database.models import db, Users, RequestsHotels, RequestsRestaurants, RequestsAttractions, LocationId


def init_db():
    """
    Инициализация базы данных
    """
    db.connect()
    db.create_tables([Users, RequestsHotels, RequestsRestaurants, RequestsAttractions, LocationId])


def close_db():
    """
    Закрытие базы данных
    :return:
    """
    db.close()


def check_user_db(first_name: str):
    """
    Проверка наличия пользователя в базе данных
    :param first_name: имя пользователя
    :return: bool
    """
    if Users.select(Users.first_name).where(Users.first_name == first_name):
        return Users.get(Users.first_name == first_name)
    return False


def check_city_db(city: str):
    """
    Проверка наличия города в базе данных
    :param city: город
    :return: bool
    """
    if LocationId.select(LocationId.city).where(LocationId.city == city):
        return True
    return False


def record_user_db(username: str, first_name: str):
    """
    Занесение пользователя в базу данных. Предварительно проверяем его наличие в таблице
    :param username: username пользователя
    :param first_name: имя пользователя
    """
    if not check_user_db(first_name):
        first_name = json.dumps(first_name, ensure_ascii=False)
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
    table(date=date, user_id=user_id, request=json.dumps(request, ensure_ascii=False)).save()


def record_location_city(location_city):
    """
    Запись location_id города в базу данных
    :param location_city: location_id города
    """
    location_id, city = location_city[0], location_city[1].lower()
    if not check_city_db(city):
        LocationId(location_id=location_id, city=city).save()


def read_location_city_from_db(city):
    """
    Получение location_id города из базы
    :param city: наименование города
    :return: location_id города
    """
    city = city.lower()
    if LocationId.select(LocationId.location_id).where(LocationId.city == city):
        return LocationId.get(LocationId.city == city).location_id
    return False


def read_data_of_restaurants(first_name, count=1):
    """
    Получение данных по ресторанам из базы
    :param first_name: имя пользователя
    :param count: количество записей
    """
    user_id = check_user_db(first_name)
    if user_id:
        data = RequestsRestaurants.select().where(RequestsRestaurants.user_id == user_id).\
            order_by(RequestsRestaurants.id.desc()).limit(count)
        for i_data in data:
            i_data = json.loads(i_data.request)
            for i_result in i_data:
                data_of_restaurant, coordinates = i_result
                yield data_of_restaurant, coordinates


# if __name__ == "__main__":
#     # db.connect()
#     print(check_city_db('Pattaya'))
#     # print(check_user('Alex'))
