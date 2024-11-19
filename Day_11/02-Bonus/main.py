# Creamos una función que obtiene números de un archivo de texto y devuelve la media de esos números
import os

path = os.path.join(os.path.dirname(__file__), 'files/data.txt')

def get_average():
    with open(path, 'r') as file:
        data = file.readlines()
        
    # Nos quedamos solo con los valores numéricos, desechando el texto temperatures
    values = data[1:]
    # Transformamos cada valor a numérico (quita automáticamente el \n de cada elemento)
    values = [float(i) for i in values]
    
    average_local = sum(values) / len(values)
    return average_local
    
    
average = get_average()
print(average)
