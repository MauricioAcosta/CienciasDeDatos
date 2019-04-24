# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:02:18 2018

@author: Nelson
"""

import numpy as np

#1D
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# INDEX 1D
print(x[3])
print(x[-2])


# SLICING 1D
print(x[1:7:2])

print(x[-2:10])

print(x[-3:3:-1])

#2D

y = np.arange(20).reshape(5,4)
print(y)

# INDEX 2D

#simple
print(y[2,1])

#double
n = y[[1,2,3],[0,3,1]]
print(n)


# SLICING 2D

# 2D->1D
print(y[1:2, 1:3])

# 2D->2D
print(y[1:3, 1:3])


#3D

z = np.arange(40).reshape(2,5,4)
print(z)

# INDEX 3D

#simple
print(z[1,3,2])


#triple

print(z[0:2,0:3,0:3])


