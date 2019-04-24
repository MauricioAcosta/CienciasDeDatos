# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
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
            #aux = imagen[i][j]*mascara[i][j]
            pass
            
    

img = mpimg.imread('/home/estudiantes/Imágenes/CienciasDeDatos/taller3/image.png')
mascara = np.full((3,3),1/9)          
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
print(gray.shape)
recorrer(gray,mascara)



