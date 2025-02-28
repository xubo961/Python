# 1. Leer el contenido de una carpeta diferenciando entre ficheros y directorios (Utilizando os)
import os

ruta = ".."

for fichero in os.listdir(ruta):
    rutaFichero = os.path.join(ruta, fichero)
    if os.path.isfile(rutaFichero):
        print(f"{fichero} es un fichero")
    if os.path.isdir(rutaFichero):
        print(f"{fichero} es un archivo")
    else:
        print("Desconocido")
