# Vemos el módulo csv
import csv, os

path = os.path.dirname(__file__)

with open(f"{path}/files/weather.csv", 'r') as file:
    # csv.reader(file) devuelve un tipo iterator, que
    # convertimos a un tipo lista.
    data = list(csv.reader(file))

# Para probar informar: New York
city = input("Enter a city: ")

# Iteramos desde el índice 1 para no tener en cuenta la cabecera.
for row in data[1:]:
    if row[0] == city:
        print(row[1])