# DIVIDE el CSV en x CSVs de 500 lineas cada uno 
import pandas as pd 
for i,chunk in enumerate(pd.read_csv('Diagn_sticos_emitidos.csv', chunksize=500)):
    chunk.to_csv('Diagn_sticos_emitidos{}.csv'.format(i))
