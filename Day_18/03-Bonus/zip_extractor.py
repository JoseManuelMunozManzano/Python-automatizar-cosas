import zipfile, pathlib

def extract_archive(archivepath, dest_dir):    
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    import os
     
    path = os.path.dirname(__file__)
    archivepath = pathlib.Path(path, "compressed.zip")
    destination = pathlib.Path(path, "dest")
    extract_archive(archivepath, destination)