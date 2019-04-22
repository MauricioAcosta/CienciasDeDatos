import numpy as np
z = np.arange(729).reshape(9, 9, 9)

def limites(limite1, limite2):
    cara =  z[0:9, limite1:limite1+3, limite1:limite1+3]
    z[0:9, limite1:limite1+3, limite1:limite1+3] = z[0:9, limite2:limite2+3, limite2:limite2+3]
    z[0:9, limite2:limite2+3, limite2:limite2+3] = cara
    return z

num1 = int(input('Ingresa limite 1: '))
num2 = int(input('Ingresa limite 2: '))
print(limites(num1, num2))
