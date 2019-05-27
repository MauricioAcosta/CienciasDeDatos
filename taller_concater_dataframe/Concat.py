# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import pandas as pd

# CONCATENACIÓN VERTICAL

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3'],
'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']},index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7'],
'C': ['C4', 'C5', 'C6', 'C7'],'D': ['D4', 'D5', 'D6', 'D7']},index=[4, 5, 6, 7])

frames=[df1,df2]
dfv=pd.concat(frames, axis=0) # axis=0 por defecto
print(df1)
print(df2)
print(dfv)

# CONCATENACIÓN HORIZONTAL

df3 = pd.DataFrame({'E': ['E0', 'E1', 'E2', 'E3'],'F': ['F0', 'F1', 'F2', 'F3'],
'G': ['G0', 'G1', 'G2', 'G3'],'H': ['H0', 'H1', 'H2', 'H3']},index=[0, 1, 2, 3])

frames=[df1,df3]
dfh=pd.concat(frames, axis=1)
print(df1)
print(df3)
print(dfh)

# INNER Y OUTER


df4 = pd.DataFrame({'A': ['A2', 'A3', 'A6', 'A7'],'C': ['C2', 'C3', 'C6', 'C7'],
'G': ['G2', 'G3', 'C6', 'C7'],'H': ['H2', 'H2', 'D6', 'D7']},index=[2, 3, 6, 7])


frames=[df1,df4]
dfv=pd.concat(frames, axis=0, join='outer') #join='outer' por defecto
print(df1)
print(df4)
print(dfv)

dfh=pd.concat(frames, axis=1, join='outer') #join='outer' por defecto
print(df1)
print(df4)
print(dfh)

frames=[df1,df4]
dfv=pd.concat(frames, axis=0, join='inner')
print(df1)
print(df4)
print(dfv)

dfh=pd.concat(frames, axis=1, join='inner') 
print(df1)
print(df4)
print(dfh)

# EXACT INDEX / EXACT COLUMNS

dfh = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
print(df1)
print(df4)
print(dfh)

dfv = pd.concat([df1, df4], axis=0, join_axes=[df1.columns])
print(df1)
print(df4)
print(dfv)

# IGNORE INDEX

dfV = pd.concat([df1, df4], axis=0, ignore_index = True)
print(df1)
print(df4)
print(dfV)

dfh = pd.concat([df1, df4], axis=1, ignore_index = True)
print(df1)
print(df4)
print(dfh)

# CONCATENANDO CON APPEND

dfv=df1.append(df4)
print(df1)
print(df4)
print(dfv)

dfv=df1.append(df4, ignore_index=True)
print(df1)
print(df4)
print(dfv)
