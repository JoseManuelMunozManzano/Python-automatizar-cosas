import requests
from datetime import datetime
import time

# El usuario va a indicar las fechas desde y hasta que quiere, y el ticker
ticker = input("Enter the ticker symbol (AAPL, MSFT...): ")
from_date = input('Enter start date in yyyy-mm-dd format: ')
to_date = input('Enter end date in yyyy-mm-dd format: ')

# Aunque para este programa no vale, aquí se muestra una forma de transformar
# una fecha string a epoch
from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
to_datetime = datetime.strptime(to_date, '%Y-%m-%d')

from_epoch = time.mktime(from_datetime.timetuple())
to_epoch = time.mktime(to_datetime.timetuple())
print(f"From_Datetime to Epoch = {from_epoch}")
print(f"To_Datetime to Epoch = {to_epoch}")

url = f"https://api.nasdaq.com/api/quote/{ticker}/historical?assetclass=stocks&fromdate={from_date}&limit=9999&todate={to_date}&random=24"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

# Obtenemos un byte object.
# Si en vez de content se usa text, obtenemos texto, pero el uso más generalizado
# indica obtener bytes.
content = requests.get(url, headers=headers).content
# print(content)

# Creamos un archivo vacío y escribimos esos bytes en el archivo.
with open("data.json", 'wb') as file:
    file.write(content)
    
