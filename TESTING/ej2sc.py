# Escriba una función recursiva que devuelva la cantidad de hojas de un árbol binario

from Arbol import ArbolB

def nodosHojasR(arbol):
    cuenta=0
    if(arbol.izq == None and arbol.der == None):
        return 1
    else:
        if(arbol.izq != None):
            cuenta += nodosHojasR(arbol.izq)
        if(arbol.der != None):
            cuenta += nodosHojasR(arbol.der)
    return cuenta

#miarbol=ArbolB(1,ArbolB(2,ArbolB(3),ArbolB(4)),ArbolB(5,ArbolB(6),ArbolB(7)))


# Estas son las 4 hojas
Arbol4 = ArbolB(4)
Arbol5 = ArbolB(5)
Arbol6 = ArbolB(6)
Arbol7 = ArbolB(7)

# Estos son los hijos directos de la raiz
Arbol2 = ArbolB(2,Arbol4,Arbol5)
Arbol3 = ArbolB(3,Arbol6,Arbol7)

# Esta es la raíz
Arbol1 = ArbolB(1,Arbol2,Arbol3)



print(nodosHojasR(Arbol1))