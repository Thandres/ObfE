import os
from zipfile import ZipFile

py_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".py")]
py_files.remove("zipper.py")
with ZipFile("scripts.zip", "w") as z:
    for file in py_files:
        z.write(file)
