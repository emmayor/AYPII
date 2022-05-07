class ArbolBB:
    """Define un árbol binario"""
    def __init__(self,dato,izq = None,der = None):
        self.dato = dato
        self.izq = izq
        self.der = der
    def __str__(self):
        return str(self.dato)
    def izquierdo(self,dato):
        self.izq = ArbolBB(dato)
    def derecho(self,dato):
        self.der = ArbolBB(dato)
    def subizq(self):
        return self.izq
    def subder(self):
        return self.der
    def valor(self):
        return self.dato
    def printAsc(self):
        if self.izq != None:
            self.izq.printAsc()
        print(self,end=" ")
        if self.der != None:
            self.der.printAsc()
        print()
    def insertar(self,x):
        """ Agrega un nuevo subárbol con el dato x """
        if x < self.dato:
            if self.izq == None:
                self.izq = ArbolBB(x)
            else:
                self.izq.insertar(x)
        else:
            if self.der == None:
                self.der = ArbolBB(x)
            else:
                self.der.insertar(x)
    def eliminar(self,x):
        """ Elimina elementos del árbol. (Reemplaza su valor con el mayor de su izquierda o el menor de su derecha)"""


def sizeA(arbol):
    if arbol == None:
        return 0
    return 1 + sizeA(arbol.izq) + sizeA(arbol.der)  

def alturaA(arbol):
    """ Calcula la altura del árbol, que es el camino más largo """
    """ de la raíz a una hoja """
    """ Se eligió ls implementación como función, no es un método """

    if arbol == None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)
    return 1 + max(alt_izq, alt_der)
