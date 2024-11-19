# Cada día que se ejecute el programa, se generará en la carpeta journal un archivo
# con el formato yyyy-mm-dd.txt
import os


date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10?: ")
thoughts = input("Let your thoughts flow:\n")

path = os.path.join(os.path.dirname(__file__), f"journal/{date}.txt")

with open(path, 'w') as file:
    file.write(mood + (2 * '\n'))
    file.write(thoughts)