import requests
from pprint import pprint


def get_weather(city, token):
    try:
        r = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={token}&q={city}&days=7&aqi=no&alerts=no&lang=ru')
        data = r.json()
        return data

    except Exception as ex:
        print(ex)
        print("Проверить название города")

