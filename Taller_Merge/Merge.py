# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:48:10 2019

@author: Nelson
"""

import pandas as pd

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],'value': [5, 6, 7, 8]})

# Uso del ON

df1 = pd.DataFrame({'cc': [932, 950, 940, 910],'nombre': ['Pedro','Nelson','Camilo','Tatiana'],'edad': [23,39,33,29]})
df2 = pd.DataFrame({'cc': [910, 910, 950, 940, 950, 930],'producto': ['pola', 'leche', 'pañales', 'arroz', 'pan', 'pola']})
print(df1)
print(df2)

dft=df1.merge(df2, on='cc')
print(dft)

# Uso del left_on right_on

df2 = pd.DataFrame({'cliente': [910, 910, 950, 940, 950, 930],'producto': ['pola', 'leche', 'pañales', 'arroz', 'pan', 'pola']})
dft=df1.merge(df2, left_on='cc', right_on='cliente')
print(dft)

# uso de how

df1 = pd.DataFrame({'cc': [932, 950, 940, 910],'nombre': ['Pedro','Nelson','Camilo','Tatiana'],'edad': [23,39,33,29]})
df2 = pd.DataFrame({'cc': [910, 910, 950, 940, 950, 930],'producto': ['pola', 'leche', 'pañales', 'arroz', 'pan', 'pola']})
print(df1)
print(df2)

dft=df1.merge(df2, on='cc', how='inner')
print(dft)

dft=df1.merge(df2, on='cc', how='outer')
print(dft)

dft=df1.merge(df2, on='cc', how='left')
print(dft)

dft=df1.merge(df2, on='cc', how='right')
print(dft)

# Uso de suffixes


df1 = pd.DataFrame({'cc': [932, 950, 940, 910],'nombre': ['Pedro','Nelson','Camilo','Tatiana'],'edad': [23,39,33,29],'ciudad': ['Bogotá','Ibagué','Cali','Bogotá'] })
df2 = pd.DataFrame({'cc': [910, 910, 950, 940, 950, 930],'producto': ['pola', 'leche', 'pañales', 'arroz', 'pan', 'pola'], 'ciudad': ['Bogotá','Bogotá','Medellín','Bogotá','Cartagena','Barranquilla']})
print(df1)
print(df2)

dft=df1.merge(df2, on='cc', suffixes=('_nacimiento', '_compra'))
print(dft)





