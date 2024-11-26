from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    # Obtenemos el código fuente de la página y se lo pasamos a Beautiful Soup para que lo
    # parsee usando un parser de HTML.
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    # Como queremos el valor del rate, hemos visto que está en un span con ese nombre
    # de clase. De ahí obtenemos el texto, que corresponde al valor del rate.
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    # Como el valor obtenido incluye la moneda, por ejemplo 1.613345 AUD, queremos
    # eliminar la moneda y que solo quede el valor, que transformaremos a float.
    rate = float(rate[:-4])
    
    return rate
    

current_rate = get_currency('EUR', 'AUD')
print(current_rate)