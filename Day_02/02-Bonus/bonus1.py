# Introducir password (pass123) e intentar adivinarlo
password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")