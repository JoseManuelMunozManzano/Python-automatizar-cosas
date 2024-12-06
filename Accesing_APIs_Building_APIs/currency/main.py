from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_ = "ccOutputRslt").get_text()
    rate = float(rate[:-4])
    
    return rate


# Creamos la instancia de la app
app = Flask(__name__)

# Tenemos dos endpoints:
# Uno es el homepage con la documentación de nuestra API.
@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

# El segundo endpoint es el que realmente da la funcionalidad para transformar un importe a otro.
# Utilizamos dos path variables, in_cur y out_cur
@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    # Utilizar un diccionario es una buena práctica para servir este tipo de datos a través de las API
    result_dictionary = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    # Devolvemos un json a partir del diccionario
    return jsonify(result_dictionary)


app.run()
