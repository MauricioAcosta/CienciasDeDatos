#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:35:14 2019

@author: leidy_aldana
"""

import numpy as np
from PIL import Image, ImageOps

color_nuevo = (0,172,193)
color_actual = (33,150,243)
 
icono = Image.open('./image.png')
icono.show()
flipeada = ImageOps.flip(icono)
flipeada.show()

#b = np.full((3,3),5)
#b = np.random.random((3,3))
#print(b)
#b= np.append(b, b[:,0], axis=0)
array=[1,2,3]
array2=[4,5,6,7,8]
#b = np.insert(b, 0, b[:,0], axis=0)
#b = np.resize(b,(b.shape[0]+1,b.shape[1]+1))

# Duplicando valores para x
b = np.insert(b, 0, b[0,:], axis=0)
b = np.insert(b, b.shape[0], b[(b.shape[0]-1),:], axis=0)
#print(b)
print("Forma de b: ")
#print(b.shape)
# Duplicando valores para y
b = np.insert(b, 0, b[:,0], axis=1)
b = np.insert(b, b.shape[1], b[:,(b.shape[1]-1)], axis=1)
#print(b)
mascara = np.full((3,3),1/5) 
#print ("Slice: ",b.shape) 
#print(b[0:(1+3),0:(1+3)])
#print(b)
elem=0
#print (mascara)
#for i in range(0, (b.shape[0]-2)):
 #   for j in range(0, (b.shape[1]-2)):
  #      aux = b[(i):(i+3),(j):(j+3)]*mascara 
        #print(np.sum(aux))
   #     b[i+1][j+1]=np.sum(aux)

#b = b.reshape(12,12)
#print(b.shape)
            
        


