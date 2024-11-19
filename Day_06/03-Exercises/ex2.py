import os

path = os.path.dirname(__file__)

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"{path}/{filename}", 'w')
    file.write("Hello")
    file.close()