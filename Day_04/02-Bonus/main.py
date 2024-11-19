# Queremos cambiar el primer punto por un guión
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# Las listas son mutables y los str son inmutables
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

# Ejemplo de tupla
# En vez de corchetes (listas), se usan paréntesis
# Son inmutables
filenames_tuple = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")