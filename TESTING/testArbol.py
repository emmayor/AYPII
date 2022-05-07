from Arbol import *

arbol1 = ArbolB('*',ArbolB('+',ArbolB(3),ArbolB(7)),ArbolB(9))
arbol2 = ArbolB('+',ArbolB(3),ArbolB('*',ArbolB(7),ArbolB(9)))

arbol1.printInfijo()
print()
arbol2.printInfijo()



ArbolHijoIzq = ArbolB('Soy el hijo Izquierdo')
ArbolHijoDer = ArbolB('Soy el hijo Derecho')
ArbolPadre = ArbolB('Soy el padre',ArbolHijoIzq, ArbolHijoDer)