import numpy as np
z = np.arange(729).reshape(9,9,9)
def limites(id1,id2):
    a=np.where(z==id1)
    b=np.where(z==id2)
    print(a)
    num1=z[a[0],a[1],a[2]]
    z[a[0],a[1],a[2]]=z[b[0],b[1],b[2]]
    z[b[0],b[1],b[2]]=num1
    return z

num1=int(input('Ingresa numero 1: '))
num2=int(input('Ingresa numero 2: '))
print(limites(num1,num2))