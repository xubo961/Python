import os

if os.path.isdir("Documento.txt"):
    print("Es directorio")

if os.path.isfile("Documento.txt"):
    print("Es fichero")

if os.path.exists("documento.txt"):
    print("Documento existe")
    f = open('documento.txt', "a")
    f.write("Documento existe\n")
else:
    print("Documento no existe")
    f = open('documento.txt', "x")

f.close()