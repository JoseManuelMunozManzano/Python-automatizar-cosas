# Creamos funciones que conviertan la entrada del usuario en metros.
# En función del resultado, permitirá a un niño montarse en una atracción de feria.
#
# Siempre tendremos en cuenta hacer el programa desacoplado.
# La salida de una función debe estar desacoplada de otros componentes.
# Esto es lo mismo que decir que las salidas de las funciones deben ser cosas sencillas, como valores,
# no salidas complejas, como cadenas de texto personalizadas, porque no son reutilizables.
#
# Otra cosa muy importante sobre la funciones es que deben hacer solo una cosa.
# Por tanto, habrá que dividir una función en tantas como sean necesarias con ese objetivo.
# Esto hace más legible el código y más fácil de depurar si hay errores.
#
# Ejemplo de entrada: 5 12
# Resultado: Kid can use the slide.
feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_arg):
    """ Return a tuple with the feet and inches """
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    """ Given feet and inches, returns meters """
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet, inches = parse(feet_inches)
result = convert(feet, inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")