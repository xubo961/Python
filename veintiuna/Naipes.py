from random import shuffle

from CalculoSalario import nombre
from veintiuna.Carta import Carta

# Objetivo: Llegar a 21 sin pasarse
# Juegas contra la casa
# Te puedes plantar siempre que no hayas llegado a 21
# o seguir pidiendo cartas
# La casa se planta cuando tiene 17 o más
# A = 1, 11
# J, Q, K = 10
# 2..10 = Su valor

baraja = []
manoJugador = []
manoCasa = []
sePlanta = False


def llenarBaraja(baraja):
    palos = ["♥️", "♣️", " ♠️", "♦️"]
    for i in range(4):
        for j in range(1, 14):
            palo = palos[i]
            valor = 0
            nombre = ""
            if j < 11:
                valor = j
                nombre = f"{j} de {palo}"
            elif j > 10:
                valor = 10
                if j == 11:
                    nombre = f"J de {palo}"
                elif j == 12:
                    nombre = f"Q de {palo}"
                elif j == 13:
                    nombre = f"K de {palo}"
            carta = Carta(palo, valor, nombre)
            baraja.append(carta)


def repartir(numCartas, mano):
    for i in range(numCartas):
        mano.append(baraja.pop())


def sePasa(mano):
    return sumarValores(mano) > 21


def sumarValores(mano):
    valoresMano = 0
    for carta in mano:
        valoresMano += carta.valor
    return valoresMano


def jugar():
    if (input("Quieress otra? (s/n)").lower() == "s"):
        repartir(1, manoJugador)
        print(manoJugador)
    else:
        global sePlanta
        sePlanta = True


def juegaLaCasa():
    imprimirCartas(manoCasa)
    valorCasa = sumarValores(manoCasa)
    while (valorCasa < 17 | valorCasa < sumarValores(manoJugador)):
        repartir(1, manoCasa)
        imprimirCartas(manoCasa)
        valorCasa = sumarValores(manoCasa)


def imprimirCartas(mano):
    for carta in mano:
        print(carta)


llenarBaraja(baraja)
shuffle(baraja)
repartir(2, manoJugador)
repartir(2, manoCasa)

print(f"Jugador: ")
imprimirCartas(manoJugador)
print(f"Casa:")
print(manoCasa[0], "\n?")

while not sePlanta and not sePasa(manoJugador):
    jugar()
    if (sePlanta and not sePasa(manoJugador)):
        juegaLaCasa()

if not sePasa(manoCasa):
    print("Gana la casa")
else:
    print(f"Gana el jugador con {sumarValores(manoJugador)}")
    print(f"Gana el jugador con {sumarValores(manoJugador)}")

print(f"J: {imprimirCartas(manoJugador)}")
print(f"J: {imprimirCartas(manoCasa)}")