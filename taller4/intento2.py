"""
Autores:
    Andrés Mauricio Acosta Pulido - 20142020111
    Leidy Marcela Aldana Burgos - 20151020019
Programa de manejo de imagenes con Numpy
Objetivo: Desarrollar un efecto sobre una imagen
Versión 2. Implementación de Efecto .^^.
Realizado haciendo uso de: Editor de Spyder
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#b = np.zeros((300,300))
desorden=np.arange(16).reshape(4,4)
np.random.shuffle(desorden)

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def comb(matA, matB):
    return np.array(np.meshgrid(matA, matB)).T.reshape(-1, 3)

def recorrer(imagen, elementos):
    for i in range(0, 4):
        for j in range(0, 4):
            x = (i)*elementos
            y = (j)*elementos
            partes=imagen[x:x+elementos,y:y+elementos]
            insertar(partes)
    return partes

def insertar(partes):
    
    
# Leyendo la imagen
img = mpimg.imread('./image.png')

gray = rgb2gray(img)
gray = gray[:gray.shape[0]-15,:gray.shape[0]-15]

plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

elementos=(gray.shape[0]//4)
partes=recorrer(gray, elementos)

