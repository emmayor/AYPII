# Diseñar y escribir una función que determine si un número natural (entero mayor que 1) es o no primo.
# Luego escribir el programa que lea un número ingresado por teclado y, utilizando la función previamente escrita,
# determine si es primo o no. El algoritmo deberá continuar pidiendo números, hasta que el usuario ingrese un
# número 0. En ese caso, se debe confirmar la salida del programa, dando al usuario la posibilidad de seguir
# ingresando números.

from math import sqrt, floor

n = 1

# Se decide verificar n % i == 0 hasta que i sea el entero más cercano por izquierda de la raíz cuadrada del número.

def esPrimo(n):
    for i in range(2,1+floor(sqrt(n))):
        # print(str(i)+', ',end='')
        if (n % i == 0):
            return False
    return True

while n != 0:
    n = int(input("Ingrese un número mayor a 1 (0 para salir)\n> "))
    if n != 0:
        if n <= 1:
            print("El número debe ser mayor a 1!")
        else:
            if esPrimo(n):
                print("El número ES primo!")
            else: 
                print("El número NO ES primo!")
   