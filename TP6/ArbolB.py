class ArbolB:
    """Define un árbol binario"""
    def __init__(self,dato,izq = None,der = None):
        self.dato = dato
        self.izq = izq
        self.der = der
    def __str__(self):
        return str(self.dato)
    def izquierdo(self,dato):
        self.izq = ArbolB(dato)
    def derecho(self,dato):
        self.der = ArbolB(dato)
    def printInfijo(self):
        if self.izq != None:
            self.izq.printInfijo()
        print(self,end=" ")
        if self.der != None:
            self.der.printInfijo()
    def printRpn(self):
        if self.izq != None:
            self.izq.printRpn()
        if self.der != None:
            self.der.printRpn()
        print(self,end=" ")
    def printPn(self):
        print(self,end=" ")
        if self.izq != None:
            self.izq.printPn()
        if self.der != None:
            self.der.printPn()

def sizeA(arbol):
    if arbol == None:
        return 0
    return 1 + sizeA(arbol.izq) + sizeA(arbol.der)  
