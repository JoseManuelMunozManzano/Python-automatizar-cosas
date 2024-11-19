# Vamos a crear, para cada elemento de contents, su archivo filename en la carpeta files(
# Uso de la función zip()
import os

path = os.path.join(os.path.dirname(__file__), 'files')

contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{path}/{filename}", 'w')
    file.write(content)
    file.close()

# Dividiendo un string en distintas líneas
a = "I am a string " \
    "on my own"