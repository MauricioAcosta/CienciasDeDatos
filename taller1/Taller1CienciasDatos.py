import random

numeroAleatorio=random.randrange(0,100)
intentos=10
while intentos!=0:
    try:
        numUsuario=int(input("Adivina el número entre 0 a 99\n")) 
        if numUsuario==numeroAleatorio:
            print("Felicidades, tu puntaje es: ",intentos)
            break
        elif numeroAleatorio>numUsuario:
            print("El número a adivinar es mayor")
        elif numeroAleatorio<numUsuario:
            print("El número a adivinar es menor")
        else:
            print("No es el número\nTe quedan ",intentos-1)       
    except:
        print("Ingresaste un caracter invalido")
    intentos=intentos-1
else:
    print("Perdiste, tu puntaje es: ",intentos)