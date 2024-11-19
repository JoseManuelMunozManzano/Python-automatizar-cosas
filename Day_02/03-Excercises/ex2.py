# Create a program that:
# (1) prompts the user to input their name,
# (2) prints out the name with the first letter capitalized,
# (3) keeps prompting the user to input another name
# (4) prints out the name with all letters capitalized,
# (5) The process is repeated infinitely.

name = input("Write your name: ")
print(name.capitalize())

while True:
    name = input("Write your name: ")
    print(name.upper())