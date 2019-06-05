# DIVIDE el CSV en x CSVs de 500 lineas cada uno 
import pandas as pd 
for i,chunk in enumerate(pd.read_csv('C_DIGO__NICO_DE_MEDICAMENTOS_VIGENTES.csv', chunksize=500)):
    chunk.to_csv('C_DIGO__NICO_DE_MEDICAMENTOS_VIGENTES{}.csv'.format(i))
