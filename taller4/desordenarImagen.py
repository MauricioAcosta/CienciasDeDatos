"""
Autores:
    Andrés Mauricio Acosta Pulido - 20142020111
    Leidy Marcela Aldana Burgos - 20151020019
Programa de manejo de imagenes con Numpy
Objetivo: Desarrollar un programa que desordene una imagen
Realizado haciendo uso de: Editor de Spyder
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def recorrer(img, desorden):
    shuffled_image = np.array([])
    for row in range (0, 4):
        for aux in range(0, 75):
            fila = np.array([])
            for col in range(0,4):
                r1, c1 = getCords(desorden[row,col])
                fila = np.hstack((fila, img[r1+aux, c1:c1+75]))
            if( shuffled_image.shape[0] == 0): shuffled_image = fila
            else: shuffled_image = np.vstack((shuffled_image, fila))
    return shuffled_image

def getCords( num ):
    r = num // 4 
    c = num %  4 
    return r*75, c*75
# Leyendo la imagen
img = mpimg.imread('./image.png')

aux =np.arange(16)
np.random.shuffle(aux)
desorden = aux.reshape((4,4))
print(desorden)
print( getCords(15))
gray = rgb2gray(img)
gray = gray[:gray.shape[0]-15,:gray.shape[0]-15]
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

elementos=gray.shape[0]//4

partes=recorrer(gray, desorden)

#imagendesorden=unirpartes(partes)
plt.imshow(partes, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()