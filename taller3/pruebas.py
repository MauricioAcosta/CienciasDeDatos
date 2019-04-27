#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:35:14 2019

@author: leidy_aldana
"""

b = np.full((11,11),5)
mascara = np.full((3,3),1/5) 
#print ("Slice: ",b.shape) 
#print(b[0:(1+3),0:(1+3)])
#print(b)
#print (mascara)
for i in range(1, (b.shape[0]-2)):
    for j in range(1, (b.shape[0]-2)):
        aux = b[j:(j+3),i:(i+3)]*mascara 
        print(aux)
            
            
