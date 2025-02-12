""""

Máquina de bebidas
Agua - 0.50€
Refresco - 0.75€
Zumo - 0.95€

El programa emitirá un menú que mostrará productos y precios, además de la opción salir.
Pedirá la opción elegida y pedirá monedas al usuario.

La máquina acepta todas las monedas de euro de 2€ a 5cts.

Al comienzo del día la máquina dispone de todas las cantidades necesarias para el cambio.

Se debe dar el cambio correcto, con menor número posible de monedas.
La máquina mostrará un mensaje de "INTRODUZCA IMPORTE EXACTO" en caso de no tener dos tipos de monedas cualquiera
o si una de las ausentes es la pila de 5cts. Sólo aceptará el importe exacti en este caso.

Al fial del programa nos debe dar el total del dinero disponible en la máquina, por unidad monetaria.

"""

valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
resevaMonedas = [20, 20, 20, 20, 20, 20]
nombresProductos = ["Agua 🥃", "Refresco 🍾", "Zumo 🍹"]
preciosProductos = [0.50, 0.75, 0.95]


def printMenu(nombres, precios):
    if len(nombres) != len(nombres):
        return False
    textoMenu = "¡Bienvenido! ¿Que deseas?\n"
    for i in range(len(nombres)):
        textoMenu += f"{i + 1} - {nombres[i]} : {precios[i]}\n"
    textoMenu += f"{len(nombres) + 1} - Salir"
    print(textoMenu)


def elegirProducto(producto):
    opcion = input("Elija una opción => ")
    numerosProductos = []
    for i in range(len(producto)):
        numerosProductos.append(str(i + 1))

    while opcion not in numerosProductos:
        opcion = input("Elija una opción correcta => ")
    return int(opcion) - 1

def ingresarImporte(opcion):
    precio = preciosProductos[opcion]
    importeUsuario = 0
    monedasIntroduces = []
    while importeUsuario < precio:
        print(f"Le queda {round(precio - importeUsuario, 2)} por ingresar.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroduces.append(moneda)
    if importeUsuario > precio:
        resto = importeUsuario - precio
    #     darCambio(resto)
    #
    # entregarProducto(nombresProductos[opcion])
    sumarMonedas(monedasIntroduces)

#
# def darCambio(resto):
#
#
#
# def entregarProducto(nombre):
#     print(f"Aquí tiene su {nombre}")

def sumarMonedas(monedas):
    for moneda in monedas:
        resevaMonedas[valoresMonedas.index(moneda)] += 1

def ingresarMoneda():
    valoresValidos = []
    for valor in valoresMonedas:
        valoresValidos.append(str(valor))
    moneda = input("Ingrese una moneda => ")
    while moneda not in valoresValidos:
        moneda = input("Introduzca una moneda válida => ")
    return float(moneda)

printMenu(nombresProductos, preciosProductos)
opcion = elegirProducto(nombresProductos)
if opcion == len(nombresProductos) + 1:
    print("Gracias por venir")
else:
    ingresarImporte(opcion)
    print(valoresMonedas)

    print(resevaMonedas)




