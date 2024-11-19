import zipfile, pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # Para crear un nuevo fichero .zip, usamos el modo 'w' de escritura.
    # Para extraer data de un fichero .zip, usamos el modo 'r' de lectura.
    # Hay que indicar la ruta al archivo .zip que se creará, no la ruta al directorio.
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # En arcname indicamos el nombre del fichero de esa ruta.
            # El objetivo es que no comprima todo el recorrido de directorios, solo el fichero.
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":   
    import os
     
    path = os.path.dirname(__file__)
    archive1 = pathlib.Path(path, "main.py")
    archive2 = pathlib.Path(path, "zip_creator.py")
    destination = pathlib.Path(path, "dest")
    make_archive(filepaths=[archive1, archive2], dest_dir=destination)