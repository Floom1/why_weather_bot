import os
import datetime
import requests



def _get_weather(city: str) -> [int, str]:
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid=6274e07016f0f01ccfb89d192be57c44")
    data = response.json()
    cur_temp = data["main"]['temp']
    # weather = data["weather"][0]["main"]

    return cur_temp


# def get_weather(message):
#     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather? q=москва&lang=ru&units=metric&appid=6274e07016f0f01ccfb89d192be57c44")
#     return response.json()

print(_get_weather('Москва'))
