import json
from datetime import datetime

import requests
from aiogram.types import InputFile

from database.CRUD import record_request
from database.models import RequestsRestaurants
from settings import SiteApiSettings

X_RapidAPI_Key = SiteApiSettings().X_RapidAPI_Key.get_secret_value()
X_RapidAPI_Host = SiteApiSettings().X_RapidAPI_Host.get_secret_value()

# url = "https://travel-advisor.p.rapidapi.com/locations/search"



# querystring = {
#     "query": city,
#     "limit": "30",
#     "offset": "0",
#     "units": "km",
#     "location_id": "1",
#     "currency": "USD",
#     "sort": "relevance",
#     "lang": "en_US"}

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
    :return:
    """
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    querystring = {"latitude": coordinates[0], "longitude": coordinates[1], "limit": count, "currency": "RUB",
                   "distance": distance_search, "open_now": "false", "lunit": "km", "lang": "ru_RU"}
    response = requests.request("GET", url, headers=headers, params=querystring).text
    print(response)
    record_request(first_name=first_name, request=response, table=RequestsRestaurants)
    return response


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
    response = requests.request("GET", url, headers=headers, params=querystring).text
    print(response)
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
