# Ejercicio 6
# Escribí una función para mezclar dos listas enlazadas. Las listas de entrada tienen sus elementos en orden
# creciente, de menor a mayor. La lista de salida también debe quedar ordenada, pero de mayor a menor (orden
# decreciente).
# El algoritmo debería tomar tiempo lineal, según la longitud de la lista de salida, que es la suma de la longitud de
# las dos listas.
# EJ:
# L1 = [1, 12, 45, 46]
# L2 = [0, 20, 40, 60, 80, 100]
# L3 = [100, 80, 60, 46, 45, 40, 20, 12, 1, 0]

from ListaEn_Ej5 import ListaEnlazada

listaImpares = ListaEnlazada()
listaPares = ListaEnlazada()

def intercalarDesc(lista1, lista2):



