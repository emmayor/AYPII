# Implementar una función que, usando el TAD Pila, devuelva una nueva pila invertida. Es decir que el elemento que
# estaba en el tope de la pila original, ahora estará abajo de todo.

from tads import Pila

def invertirPila(pila):
    pilaInv = Pila()
    while not pila.estaVacia():
        pilaInv.apilar(pila.desapilar())
    return pilaInv

pila = Pila()

pila.apilar('1')
pila.apilar('2')
pila.apilar('3')
pila.apilar('4')

pilaInvertida = invertirPila(pila)
print(pilaInvertida)
