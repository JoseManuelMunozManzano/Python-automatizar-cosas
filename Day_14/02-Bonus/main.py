# Ejemplo de uso de módulos.
# Ejemplo de entrada: 5 12
# Resultado: Kid can use the slide.
from converters import convert
from parsers import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet and {parsed["inches"]} inches are equal to {result} meters")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")