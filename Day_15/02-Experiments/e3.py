# Vemos el módulo shutil (shell utilities)
# Se pueden copiar archivos, crear archivos zip, extraer ficheros de un zip...
import shutil, os

path = os.path.dirname(__file__)

# En el ejemplo vamos a crear un archivo zip que contenga los archivos del directorio files.
# Indicamos el nombre de salida, el tipo de archivo y la localización de los archivos a comprimir.
shutil.make_archive(f"{path}/output", "zip", f"{path}/files")