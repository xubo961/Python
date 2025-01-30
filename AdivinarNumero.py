#Juego en el que la máquina crea un n aleatorio 1.100
#El jugador intenta adivinar hasta que lo consigue
#la maquina da pistas (mas alto o mas bajo)

import random as r

numeroRandom = r.randint(1,100)
acierto = False

while not acierto:
    numero = int(input("Escribe un numero entre 1 y 100: "))
    if numeroRandom > numero :
        print("Te has quedado corto: ")
    elif numeroRandom < numero:
        print("Te has pasado: ")
    else:
        print("Has acertado")
        acierto = True






