# 5. Crear un diccionario y trabajar con sus valores (lectura, escritura)
import json

diccionariosAnidados = {
    "nobuk": "Piel curtida de vaca jajaja lol xd",
    "curtido": {
        1: "adj. jajajajaj",
        2: "kakakakak"
    },
    "legumbre": {
        1: "papapapaap"
    }
}

diccionarioConListas = {
    "nobuk": ["k. asjdhiashdaihsudha", "ñ. jasidasijdasijda", "p. qwuyeuqwuieqwye"],
    "curtido": ["l. dhuiasidasihudhgaiudasuh", "s. hfsdufhdf", "v. iqiqiqiqi"],
    "legumbre": ["askjhdashdiuasiuhdhaoid", "q. nvjusdivfsdfd", "s. daosidwqideqwij"]
}

palabraNueva = input("Ingrese una palabra o escriba 'exit': ")
while palabraNueva != "exit":
    definicion = ("Dimelon: \n")
    diccionarioConListas[palabraNueva] = [definicion]
    palabraNueva = input("Ingrese una palabra o escriba 'exit': ")

with open("diccionario.txt", "w", encoding="utf-8") as file:
    json.dump(diccionarioConListas, file, indent=4)

busqueda = input("Ingresa una busqueda: ")

if busqueda in diccionarioConListas:
    cont = 1
    for acepcion in diccionarioConListas[busqueda]:
        print(f"{cont}: {acepcion}")
        cont += 1
else:
    print("No existe la busqueda")

