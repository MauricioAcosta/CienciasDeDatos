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
    print("Empezando a recorrer: ")    
    for i in range(0, (imagen.shape[0]-2)):
        for j in range(0, (imagen.shape[0]-2)):
            aux = np.multiply( imagen[j:(j+3),i:(i+3)] , mascara)
            #print(np.sum(aux))            
            imagen[j+1][i+1]=np.sum(aux)
        
            
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


