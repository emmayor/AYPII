# Escriba una función recursiva que devuelva la cantidad de hojas de un árbol binario.

from ArbolB import ArbolB, hojas

# La misma función esta en ArbolB.py

# def hojas(arbol, cuenta=0):
#     if arbol.izq != None:
#         cuenta += hojas(arbol.izq, cuenta)
#     if arbol.der != None:
#         cuenta += hojas(arbol.der, cuenta)
#     else:
#         return 1
#     return cuenta


arbol = ArbolB(1,ArbolB(2, ArbolB(6), ArbolB(7)),ArbolB(3,ArbolB(4)))



print(hojas(arbol))



