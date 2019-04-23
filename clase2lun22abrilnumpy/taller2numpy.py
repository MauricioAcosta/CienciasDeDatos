# -*- coding: utf-8 -*-
"""
Leidy Marcela Aldana Burgos 20151020019
Andres Mauricio Acosta Pulido 20142020111
"""
import numpy as np

indices = np.array([[0, 0, 0],  # 0
                    [0, 0, 1],  # 1
                    [0, 0, 2],  # 2
                    [0, 1, 0],  # 3
                    [0, 2, 2],  # 4
                    [0, 2, 3],  # 5
                    [0, 2, 0],  # 6
                    [0, 2, 1],  # 7
                    [0, 2, 2],  # 8
                    [1, 0, 0],  # 9
                    [1, 0, 1],  # 10
                    [1, 0, 2],  # 11
                    [1, 1, 0],  # 12
                    [1, 1, 1],  # 13
                    [1, 1, 2],  # 14
                    [1, 2, 0],  # 15
                    [1, 2, 1],  # 16
                    [1, 2, 2],  # 17
                    [2, 0, 0],  # 18
                    [2, 0, 1],  # 19
                    [2, 0, 2],  # 20
                    [2, 1, 0],  # 21
                    [2, 1, 1],  # 22
                    [2, 1, 2],  # 23
                    [2, 2, 0],  # 24
                    [2, 2, 1],  # 25
                    [2, 2, 2]  # 26
                    ])


def comb(matA, matB, matC):
    return np.array(np.meshgrid(matA, matB, matC)).T.reshape(-1, 3)


def copy(indices, z):
    copia = []
    for i in indices:
        copia.append(z.item(*i))
    return copia


def reemplazo(valores, indicesareemplazar, z):
    for i, val in enumerate(valores):
        # print(indicesareemplazar[i])
        z[indicesareemplazar[i][0], indicesareemplazar[i]
            [1], indicesareemplazar[i][2]] = val


def limites(fil, col, prf):
    filas = np.arange(fil*3, fil*3+3, 1)
    columnas = np.arange(col*3, col*3+3, 1)
    profundidad = np.arange(prf*3, prf*3+3, 1)
    #print(filas, columnas, profundidad)
    return filas, columnas, profundidad


z = np.arange(729).reshape(9, 9, 9)
num1 = int(input('Ingresa indice 1: '))
num2 = int(input('Ingresa indice 2: '))
filas, columnas, profundidad = limites(*indices[num1])
combinacion1 = comb(filas, columnas, profundidad)
# print(combinacion)

copia1 = copy(combinacion1, z)
# print(copia1)

filas, columnas, profundidad = limites(*indices[num2])
combinacion2 = comb(filas, columnas, profundidad)
# print(combinacion)
copia2 = copy(combinacion2, z)
# print(copia2)

reemplazo(copia1, combinacion2, z)


reemplazo(copia2, combinacion1, z)
print(z)
# z.item(*combinacion[5])
