# 2. Leer el contennido de un fichero

with open("ejercicios.txt", "r") as fichero:
    contenido = fichero.read()
    print(contenido)