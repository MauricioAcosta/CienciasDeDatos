'''
Bioinformatica

secuencia de ADN -> A,C,T,G

generar una secuencia de 120 bases random
generar una secuencia de 20 bases random

recorrer la base de 120, con la base de 20 para encontrar el mejor alineamiento, y definir una puntuntuaciòn

    Leidy Marcela Aldana Burgos -> 20151020019
    Andres Mauricio Acosta Pulido -> 20142020111

'''

import numpy as np

cadenaSecuencia=''
cadenaClave=''
indices = np.array(['A',  # 0
                    'C',  # 1
                    'G',  # 2
                    'T',  # 3
                    ])

secuencia = np.linspace(0,3,120, dtype=int)
np.random.shuffle(secuencia)

clave = np.linspace(0,3,20, dtype=int)
np.random.shuffle(clave)


for i in secuencia:
    cadenaSecuencia=cadenaSecuencia+indices[i]

for i in clave:
    cadenaClave=cadenaClave+indices[i]

def comprobar(cadena):
    contador=0
    vector=''
    for i in range(0, len(cadena)):
            if cadena[i]==cadenaClave[i]:
                contador=contador+1 
                vector=vector+cadena[i]  
    return contador, vector

repeticiones=[]
repeticiones2=[]
for i in range(0,120):
    contador, vector=comprobar(cadenaSecuencia[i:20+i])
    repeticiones.append(vector)
    repeticiones2.append(contador)

maximoVector=max(repeticiones2)

print(cadenaSecuencia[repeticiones2.index(maximoVector):repeticiones2.index(maximoVector)+20])
print(cadenaClave)
print(max(repeticiones), maximoVector)