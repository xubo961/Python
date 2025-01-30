#Realizar un programa que pida un número entero positivo de n cifras, y qie compruebe
#si el número es capicúa

numero = input("Introduce un numero: ")
esCapicua = True
for i in range(len(numero)//2):
    if numero[i] != numero[-i-1]:
        esCapicua = False

if esCapicua:
    print("El numero es capicua")
else:
    print("El numero no es capicua")
