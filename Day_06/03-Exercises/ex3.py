import os

path = os.path.dirname(__file__)

filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"{path}/{filename}", 'r')
    print(file.read())
    file.close()
