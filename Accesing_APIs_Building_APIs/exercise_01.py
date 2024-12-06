import requests
from dotenv import load_dotenv
import os


def get_key():
    path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(path)
    return os.getenv('OPENWEATHER_API_KEY')


def save_in_file(city, date, temp, condition):
    path = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(path, 'a') as file:
        file.write(f'{city},{date},{temp},{condition}\n')


def save_weather(city, units='metric'):
    r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={get_key()}&units={units}')
    content = r.json();
    temperatures = content['list']
    for temperature in temperatures:
        date = temperature['dt_txt']
        temp = temperature['main']['temp']
        condition = temperature['weather'][0]['description']
        save_in_file(city, date, temp, condition)


if __name__ == "__main__":
    save_weather('Madrid')
