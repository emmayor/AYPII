# Implementar las tres variantes del algoritmo para calcular la sucesión de Fibonacci vistas en clase (recursiva,
# iterativa, por fórmula).

# Luego escribir una función que pida un número, ejecute las tres versiones del cálculo, y para cada una de ellas
# mida cuánto tarda la ejecución. Para esto, utilice la función time() del módulo time de Python.

from math import sqrt, floor
from time import time

def fibRecursiva(n):
    if n in (0,1):
        return n
    else:
        return fibRecursiva(n-1)+fibRecursiva(n-2)

def fibIterativa(n):
    e2 = 1
    s = 0
    for i in range(n):
        e1 = s
        s = e1+e2
        e2 = e1
    return s

def fibFormula(n):
    s = (1/sqrt(5))*(((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n)
    return floor(s)

def fibonacci_completo(n):
    res = [[0,0],[0,0],[0,0]]
    start = time()
    res[0][0] = fibRecursiva(n)
    stop = time()
    res[0][1] = stop-start

    start = time()
    res[1][0] = fibIterativa(n)
    stop = time()
    res[1][1] = stop-start

    start = time()
    res[2][0] = fibFormula(n)
    stop = time()
    res[2][1] = stop-start
    return res


n = int(input("Ingrese F(n) para calcular Fibonacci\n> "))

resultado = fibonacci_completo(n)

print(f"Metodo: Recursivo. Resultado: {resultado[0][0]}. Tiempo: {resultado[0][1]} ns")
print(f"Metodo: Iterativo. Resultado: {resultado[1][0]}. Tiempo: {resultado[1][1]} ns")
print(f"Metodo: Fórmula.   Resultado: {resultado[2][0]}. Tiempo: {resultado[2][1]} ns")
