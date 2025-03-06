# 6. Programa de registro y login. La consola pedirá un usuario y contraseña.
# Tendrá que distinguir si existe el usaurio, y si no preguntará para ver si se quiere crear
# uno nuevo. En caso de que se registre, se realizará un hash (encriptado) de la contraseña que
# quiere meter (con doblre comparación) y se guardará en un fichero diccionario (JSON) con
# los nombres de usuario y las contraseñas encriptadas. En caso de login, se comprobará que la
# contraseña es correcta y es la del usuario.
import json
import pandas


usuarios = {

}

usuario = input("Escribe 'login' o 'register': ")
if usuario == "login":
    with open("usuarios.txt", "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4)
    usuarios = input("Ingrese el nombre del usuario: ")

