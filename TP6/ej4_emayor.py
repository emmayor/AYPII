# Dado un árbol binario, se desea determinar si es de búsqueda o no. Implemente una función que lo recorra y
# devuelva False si no es un ABB, y True si realmente lo es.

from ArbolB import ArbolB, esABB

arbolDesordenado = ArbolB(5,ArbolB(53, ArbolB(1), ArbolB(4)),ArbolB(7,ArbolB(6),ArbolB(10)))
arbolOrdenado = ArbolB(5,ArbolB(3, ArbolB(1), ArbolB(4)),ArbolB(7,ArbolB(6),ArbolB(10)))

# La función ya fué agregada a la clase:

# def esABB(arbol, ordenado=True):
#     if arbol.izq != None:
#         ordenado = arbol.izq.dato < arbol.dato and esABB(arbol.izq, ordenado)
#     if ordenado:
#         if arbol.der != None:
#             ordenado = arbol.der.dato > arbol.dato and esABB(arbol.der, ordenado)
#     return ordenado

print(esABB(arbolDesordenado))
print(esABB(arbolOrdenado))


        