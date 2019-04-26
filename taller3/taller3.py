# -*- coding: utf-8 -*-
"""
Autores:
    Andrés Mauricio Acosta Pulido - 20142020111
    Leidy Marcela Aldana Burgos - 20151020019
Programa de manejo de imagenes con Numpy
Objetivo: Desarrollar un efecto sobre una imagen
Realizado haciendo uso de: Editor de Spyder
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def recorrer(imagen,mascara):
    # Slicing    
    imagen[0:3]
    print(imagen)
    for i in range(1, imagen.shape[1]):
        for j in range(1, imagen.shape[0]):            
            # Posible slicing
            aux = imagen[j][i]*mascara            
            print (aux)
            #elem=elem+aux
    return imagen
    
# Leyendo la imagen
img = mpimg.imread('./image.png')
# Declaración de máscara
mascara = np.full((3,3),1/9)          
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
print(gray.shape[0])
print(gray.shape[1])
gray=recorrer(gray,mascara)
print("Después de recorrer")
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()


