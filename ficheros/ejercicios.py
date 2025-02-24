import os

if os.path.isdir("ejercicios.txt"):
    print("Es directorio")
    f = open("ejercicios.txt", "r")
    print(f.read())

if os.path.isfile("ejercicios.txt"):
    print("Es un fichero y dice: \n")
    f = open("ejercicios.txt", "r")
    print(f.read())

    if os.path.exists("holamundo.txt"):
        f = open("holamundo.txt", "a")
        f.write("Hola mundo :D\n")
        print("\nEste  fihcero ya existe")
        print("Se ha actualizado el fichero 'holamundo.txt' y dice:\n")
        f = open("holamundo.txt", "r")
        print(f.read())
    else:
        f = open("holamundo.txt", "x")
        print("\nCreado el fichero 'holamundo.txt'")
