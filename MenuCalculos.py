"""
Mostrar el siguiente menú para que el usuario decida:
1. Calcular si el número que le pasas es primo -> %0 1 y N
2. Calcular si el número que le pasas es par -> N % N -> resto
3. Calcular si el número (año) que le pasas es bisiesto ->
    Divisible por 4.
    No divisible por 100.
    Salvo si es divisible por 400.
    (2000 y 2400 son bisiestos pues aún siendo divisibles
    por 100 lo son también por 400. Pero los años 1800,
    1900, 2100, 2200 y 2300 no lo son porque solo son
    divisibles por 100).
"""

# numero = int(input("Ingresa un número entero: "))
# opciones = input("Elige una de las siguientes opciones:  \n"
#                  "1. Calcular si el número es primo \n"
#                  "2. Calcular si el número es par. \n"
#                  "3. Calcular si el número (año) es bisiesto")
#
# if opciones == "1":
#     if numero > 1:
#         for i in range(2, int(numero / 2) + 1):
#             if (numero % i) == 0:
#                 print("Es un número primo")
#                 break
#         else:
#                 print("No es un número primo")
#
# if opciones == "2":
#     print("EL número es primo")
#
#
# if opciones == "3":
#
#     print("EL número es primo")


def printMenu():
    print("1. Calcular si el número que le pasas es primo \n"
          "2. Calcular si el número que le pasas es par \n"
          "3. Calcular si el número (año) que le pasas es bisiesto \n"
          "4. Cancelar \n"
          )
def elegirOpcion():
    eleccion = input(printMenu())
    while eleccion not in "1234":
        print("Eleccion incorrecta. ")
        eleccion = input(printMenu())
    return int(eleccion)

def esPar(num):
    return num % 2 == 0

def esPrimo(num):
    if num < 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def esBisiesto(año):
    if año % 400 == 0:
        return True
    if año % 4 == 0 and año % 100 != 0:
        return True
    return False

opcion = elegirOpcion()
numero = int(input("Introduce tu numero => "))
if opcion == 1:
    print(f"Es primo: {esPrimo(numero)}")
elif opcion == 2:
    print(f"Es par: {esPar(numero)}")
elif opcion == 3:
    print(f"Es bisiesto: {esBisiesto(numero)}")
elif opcion == 4:
    print("Hasta luego")
else:
    print("Opcion extrañamente incorrecta.")


