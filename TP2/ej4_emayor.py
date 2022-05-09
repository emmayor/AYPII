# Escribir un programa que implemente un algoritmo RECURSIVO para determinar el número de bits necesarios
# para representar un entero sin signo dado.


# OPERADORES BIT A BIT
# Se usa el '>>' para desplazar los bits usados para representar a n 1 espacio a la derecha en cada iteración.
# Los bits menos significativos son descartados. Si el número es menor o igual a 1 entonces 
# se llega al caso base y el programa devuelve el total de iteraciones realizadas, coincidiendo con el número
# de bits desplazados hasta que n = 0

def calcularBits(n):
    if n<=1:
        return 1
    else:
        return 1+calcularBits(n>>1)

num = int(input("Ingrese un número mayor a 0\n> "))
bits = calcularBits(num)
print(f"Se necesitan {bits} bits para representar al número {num} ({bin(num)})")

