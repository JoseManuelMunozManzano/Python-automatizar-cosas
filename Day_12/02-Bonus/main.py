# Creamos una función que convierta la entrada del usuario en metros.
# En función del resultado, permitirá a un niño montarse en una atracción de feria.
#
# Siempre tendremos en cuenta hacer el programa desacoplado.
# La salida de una función debe estar desacoplada de otros componentes.
# Esto es lo mismo que decir que las salidas de las funciones deben ser cosas sencillas, como valores,
# no salidas complejas, como cadenas de texto personalizadas, porque no son reutilizables.
#
# Ejemplo de entrada: 5 12
# Resultado: Kid can use the slide.
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    
    meters = feet * 0.3048 + inches * 0.0254
    # Esta salida no está desacoplada. No puedo hacer nada con el valor en metros obtenido
    # return f"{feet} feet and {inches} inches is equal to {meters} meters."
    # Esta salida si está desacoplada
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")