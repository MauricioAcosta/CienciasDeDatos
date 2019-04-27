#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:35:14 2019

@author: leidy_aldana
"""

import numpy as np

b = np.full((11,11),5)
#b= np.append(b, b[:,0], axis=0)
b[:,0]=111
print(b)
mascara = np.full((3,3),1/5) 
#print ("Slice: ",b.shape) 
#print(b[0:(1+3),0:(1+3)])
#print(b)
elem=0
#print (mascara)
for i in range(0, (b.shape[0]-2)):
    for j in range(0, (b.shape[1]-2)):
        aux = b[(i):(i+3),(j):(j+3)]*mascara 
        #print(np.sum(aux))            
        b[i+1][j+1]=np.sum(aux)
            
        


