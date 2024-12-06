from datetime import datetime, timedelta
import requests
import os


def get_key():
    path = os.path.join(os.path.dirname(__file__), './NEWS_API_KEY.txt')
    with open(path, 'r') as file:
        # Cuidado con los espacios en blanco al final, que los toma como parte de la key y falla!!!!!
        # Para eso utilizo strip(), para eliminarlos.
        return file.readline().strip()


def get_news(country):
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={get_key()}")
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE:\n{article['title']}\nDESCRIPTION\n:{article['description']}")
    return results


print(get_news(country='us'))
