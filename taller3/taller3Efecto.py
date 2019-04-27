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

def recorrer(imagen,mascara,mascara2):
    # Duplicando valores para x
    imagen = np.insert(imagen, 0, imagen[0,:], axis=0)
    imagen = np.insert(imagen, imagen.shape[0], imagen[(imagen.shape[0]-1),:], axis=0)        
    # Duplicando valores para y
    imagen = np.insert(imagen, 0, imagen[:,0], axis=1)
    imagen = np.insert(imagen, imagen.shape[1], imagen[:,(imagen.shape[1]-1)], axis=1)
    print("Empezando: ")    
    for i in range(0, (imagen.shape[0]-2)):
        for j in range(0, (imagen.shape[1]-2)):
            # Aux funciona para la mascara implementada en clase
            aux = np.multiply( imagen[i:(i+3),j:(j+3)] , mascara)            
            # Aux2 funciona con otra mascara propuesta
            aux2 = np.multiply((imagen[i:(i+3),j:(j+3)]) ,  mascara2)
            #print(np.sum(aux))            
            imagen[i+1][j+1]=np.sum(aux2)        
    return imagen
    
# Leyendo la imagen
img = mpimg.imread('./image.png')
# Declaración de máscara original
mascara = np.full((3,3),(1/9))   
mascara2= np.matrix('0.21 0 -0.45; -0.75 0.5 0.95; 0.95 0 -0.42')
#mascara2=np.insert(mascara2, 0, 1/6, axis=1)
#mascara2=np.insert(mascara2, 2, 1/6, axis=1)
#print("Mascara 2")
#print(mascara2)
#mascara = np.matrix('0.111111111 0 -0.111111111; 0.111111111 0 -0.111111111; 0.111111111 0 -0.111111111')
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
#print(gray.shape[0])
#print(gray.shape[1])
gray=recorrer(gray,mascara, mascara2)
print("Después:")
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
#plt.show()
plt.show()


