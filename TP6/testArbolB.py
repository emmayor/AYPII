from ArbolBB import ArbolBB
from arbolPrinter import ImprimirABT

a1 = [8,7,6,5,4,3,0]
a2 = [20,30,40,50,60,70]
a3 = [20,60,10,30,70,68,5,12,65]

arbol1 = ArbolBB(9)
arbol2 = ArbolBB(10)
arbol3 = ArbolBB(45)

for i in a1:
    arbol1.insertar(i)
for i in a2:
    arbol2.insertar(i)
for i in a3:
    arbol3.insertar(i)

ImprimirABT(arbol3)

