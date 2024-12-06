from datetime import datetime, timedelta
import requests
import os


def get_news(topic, from_date, to_date, language='en'):
    path = os.path.join(os.path.dirname(__file__), './NEWS_API_KEY.txt')
    with open(path, 'r') as file:
        key = file.readline()
        # Cuidado con los espacios en blanco al final, que los toma como parte de la key y falla!!!!!
        # Para eso utilizo strip(), para eliminarlos.
        key = key.strip()
        
    # La forma en la que nuestra app de Python se está comunicando con esta API es a través de parámetros de URL.
    r = requests.get(f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={key}")
    # El content viene como un diccionario. Cogemos solo el value de la key articles.
    # articles está conectado a una list de diccionarios.
    # En el ejemplo obtenemos el título del primer article.
    content = r.json()
    #print(type(content))
    print(content['articles'][0]['title'])

    # Ahora obtenemos todos los titles y description de todos los articles
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE:\n{article['title']}\nDESCRIPTION\n:{article['description']}")
    return results


to_date = datetime.today().strftime('%Y-%m-%d')
from_date = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')
print(get_news(topic='space', from_date=from_date, to_date=to_date))
