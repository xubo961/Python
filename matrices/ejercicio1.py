from matrices.matrices_utils import printMatrix

"""Haz una matriz de 10x10 de nombre tabla
carga la matriz de manera que las filas pares se rellenen con un 1
y las impares con un 0
iniciar la matriz y muestra su contenido en pantalla
"""

tabla = []
for i in range(10):
    tabla.append([])
    for j in range(10):
        if i%2 == 0:
            tabla[i].append(1)
        else:
            tabla[i].append(0)
printMatrix(tabla)

