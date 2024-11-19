# Vamos a repasar uso de listas y de f-strings, y vamos a ordenar elementos de una lista alfabéticamente
waiting_list = ["sen", "ben", "john"]

waiting_list.sort()

for index, item in enumerate(waiting_list, 1):
    row = f"{index}.{item.capitalize()}"
    print(row)