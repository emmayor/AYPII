class ArbolB:
    """Define un árbol binario"""
    def __init__(self,dato,izq = None,der = None):
        self.dato = dato
        self.izq = izq
        self.der = der
    def valor(self):
        return self.valor
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

def hojas(arbol, cuenta=0):
    if arbol.izq != None:
        cuenta += hojas(arbol.izq, cuenta)
    if arbol.der != None:
        cuenta += hojas(arbol.der, cuenta)
    else:
        return 1
    return cuenta
    
def esABB(arbol, ordenado=True):
    if arbol.izq != None:
        ordenado = arbol.izq.dato < arbol.dato and esABB(arbol.izq, ordenado)
    if ordenado:
        if arbol.der != None:
            ordenado = arbol.der.dato > arbol.dato and esABB(arbol.der, ordenado)
    return ordenado

    
        