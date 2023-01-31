import requests
from settings import SiteApiSettings

X_RapidAPI_Key = SiteApiSettings().X_RapidAPI_Key.get_secret_value()
X_RapidAPI_Host = SiteApiSettings().X_RapidAPI_Host.get_secret_value()

url = "https://travel-advisor.p.rapidapi.com/attraction-products/v2/list"

querystring = {"currency": "USD", "units": "km", "lang": "en_US"}

payload = {
    "geoId": 154998,
    "startDate": "2022-03-29",
    "endDate": "2022-03-30",
    "pax": [
        {
            "ageBand": "ADULT",
            "count": 2
        }
    ],
    "sort": "TRAVELER_FAVORITE_V2",
    "sortOrder": "asc",
    "filters": [
        {
            "id": "category",
            "value": ["11873"]
        }
    ],
    "updateToken": ""
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": X_RapidAPI_Key,
    "X-RapidAPI-Host": X_RapidAPI_Host
}

# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

# print(response.text)
