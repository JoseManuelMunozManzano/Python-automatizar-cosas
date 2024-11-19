# Vemos el módulo glob
import glob, os

path = os.path.dirname(__file__)

# Indicamos los nombres de ficheros que queremos filtrar y devuelve una lista
# Es muy útil cuando tenemos varios archivos en una carpeta y queremos realizar
# algo a cada uno de ellos.
myfiles = glob.glob(f"{path}/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
