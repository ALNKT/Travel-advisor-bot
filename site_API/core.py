from typing import Dict, Union, List

import requests

from database.CRUD import record_request
from database.models import RequestsRestaurants
from settings import SiteApiSettings


def get_restaurants(data: Dict[str, Union[str, int, List[dict]]]) -> Union[Dict[str, Union[str, int, List[dict]]], str]:
    """
    Получаем из запроса по ресторанам необходимые нам данные

    :param data: данные
    :return: словарь с данными, если данные имеются, иначе строку
    """
    if len(data['data']) > 0:
        restaurants = {}
        for i_restaurant in data['data']:
            tmp_restaurant = restaurants[i_restaurant.get('name')] = []
            if not i_restaurant.get('is_closed'):
                tmp_restaurant.append({'Открыто': 'Да'})
            else:
                tmp_restaurant.append({'Открыто': 'Нет'})
            tmp_restaurant.append({'Рейтинг': i_restaurant.get('rating')})
            tmp_restaurant.append({'Кухня': i_restaurant.get('cuisine')})
            tmp_restaurant.append({'Расстояние': i_restaurant.get('distance_string')})
            tmp_restaurant.append({'Адрес': i_restaurant.get('address')})
            tmp_restaurant.append({'Телефон': i_restaurant.get('phone')})
            tmp_restaurant.append({'Фото':
                    i_restaurant.get('photo', dict()).get('images', dict()).get('medium', dict()).get('url')})
            tmp_restaurant.append({'Сайт': i_restaurant.get('web_url')})
            if i_restaurant.get('latitude') and i_restaurant.get('longitude'):
                tmp_restaurant.append({'Координаты': (i_restaurant.get('latitude'), i_restaurant.get('longitude'))})
            else:
                tmp_restaurant.append({'Координаты': None})
        return restaurants
    return 'Данные по запросу отсутствуют. Пожалуйста, попробуйте изменить параметры запроса.'


def output_restaurants(restaurants: Dict) -> Dict:
    """
    Преобразуем данные по ресторанам в строковый тип и возвращаем данные по каждому ресторану
    :param restaurants: данные по ресторанам
    """
    for i_restaurant, i_data in restaurants.items():
        coordinates = None
        if i_restaurant is not None:
            data_of_restaurant = f'Ресторан: {i_restaurant}\n'
        else:
            data_of_restaurant = f'Ресторан: Нет названия\n'
        for j_dict in i_data:
            data = {key: value for key, value in j_dict.items() if value is not None and len(value) > 0 and key != 'Координаты'}
            if j_dict.get('Кухня'):
                cuisine = [i_cuisine['name'] for i_cuisine in j_dict.get('Кухня')]
                data['Кухня'] = ', '.join(cuisine)
            if len(data) > 0:
                for key, value in data.items():
                    data_of_restaurant += f'{key}: {value}\n'
            if j_dict.get('Координаты'):
                coordinates = j_dict.get('Координаты')
        yield data_of_restaurant, coordinates


X_RapidAPI_Key = SiteApiSettings().X_RapidAPI_Key.get_secret_value()
X_RapidAPI_Host = SiteApiSettings().X_RapidAPI_Host.get_secret_value()

headers = {
    "X-RapidAPI-Key": X_RapidAPI_Key,
    "X-RapidAPI-Host": X_RapidAPI_Host
}


def nearest_restaurants(first_name: str, coordinates: tuple, distance_search: int, count: int):
    """
    Поиск ресторанов по координатам (поблизости)

    :param first_name: имя пользователя
    :param coordinates: координаты пользователя
    :param distance_search: дистанция поиска (максимум 10 км)
    :param count: количество выдаваемых результатов (максимум 30)
    """
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"
    querystring = {"latitude": coordinates[0], "longitude": coordinates[1], "limit": count, "currency": "RUB",
                   "distance": distance_search, "open_now": "false", "lunit": "km", "lang": "ru_RU"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    result_response = get_restaurants(response)
    record_request(first_name=first_name, request=result_response, table=RequestsRestaurants)
    if isinstance(result_response, str):
        yield result_response, None
    else:
        for i_date in output_restaurants(result_response):
            yield i_date


def search_restaurants(first_name: str, city: str, count: int):
    """
    Поиск ресторанов по городу

    :param first_name: имя пользователя
    :param city: город
    :param count: количество выдаваемых результатов (максимум 30)
    :return:
    """
    url = "https://travel-advisor.p.rapidapi.com/locations/search"
    querystring = {"query": city, "limit": count, "offset": "0", "units": "km", "location_id": "1",
                   "currency": "RUB", "sort": "relevance", "lang": "ru_RU"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    record_request(first_name=first_name, request=response, table=RequestsRestaurants)
    return response

# if __name__ == "__main__":
#     with open('../restaurants.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         print(data)
#         name = data['data'][0]['name']
#         photo = InputFile(data['data'][0]['photo']['images']['medium']['url'])
#         distance = data['data'][0]['distance_string']
#         phone = data['data'][0]['phone']
#         address = data['data'][0]['address']
#         print(name, photo, distance, phone, address)
#
#         str_data = data['data'][0]['name']
#     with open('res.json', 'r', encoding='utf-8') as file:
#         response = json.load(file)
