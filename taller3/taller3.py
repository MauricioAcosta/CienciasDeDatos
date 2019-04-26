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
    for i in range(imagen.shape):
        for j in range(imagen.shape[1]):
            # Posible slicing
            aux = imagen[i:3][j:3]*mascara
            print (aux)
    
# Leyendo la imagen
img = mpimg.imread('/home/estudiantes/Imágenes/CienciasDeDatos/taller3/image.png')
# Declaración de máscara
mascara = np.full((3,3),1/9)          
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
print(gray)
recorrer(gray,mascara)



