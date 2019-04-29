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

def efectoImagen(icono):     
    pass

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def comb(matA, matB):
    return np.array(np.meshgrid(matA, matB)).T.reshape(-1, 3)

def recorrer(imagen, elementos):
    for i in range(0, 4):
        for j in range(0, 4):
            x = (i)*elementos
            y = (j)*elementos
            aux=imagen[x:x+elementos,y:y+elementos]
            cara+[i,j]=aux
            print(cara)
            plt.imshow(aux, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
            plt.show()
    
# Leyendo la imagen
img = mpimg.imread('./image.png')

gray = rgb2gray(img)

gray = gray[:gray.shape[0]-15,:gray.shape[0]-15]
print(gray)        
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
print(gray.shape[0])
elementos=gray.shape[0]//4
recorrer(gray, elementos)

