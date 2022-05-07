from ArbolB import ArbolB

arbol1 = ArbolB('*',ArbolB('+',ArbolB(3),ArbolB(7)),ArbolB(9))
arbol2 = ArbolB('+',ArbolB(3),ArbolB('*',ArbolB(7),ArbolB(9)))

arbol1.printInfijo()
print()
arbol2.printInfijo()


