# Escriba una función recursiva llamada imprimirRango que, dado un ABB, un valor_bajo 
# y un valor_ alto, imprima en forma ordenada todos los nodos cuyos valores estén 
# entre valor_bajo y valor_alto. La función debería visitar la menor cantidad de nodos 
# posibles en el ABB.

from ArbolBB import ArbolBB
arbol = ArbolBB(5,ArbolBB(3, ArbolBB(1), ArbolBB(4)),ArbolBB(7,ArbolBB(6),ArbolBB(10)))

#Se consideran a ambas cotas CERRADAS
def imprimirRango(arbol, valor_bajo, valor_alto):
    if arbol.subizq() != None:
        imprimirRango(arbol.subizq(), valor_bajo, valor_alto)
    if arbol.subder() != None:
        imprimirRango(arbol.subder(), valor_bajo, valor_alto)
    if arbol.valor() in range(valor_bajo,valor_alto+1):
        print(arbol.valor())
    
imprimirRango(arbol, 4, 10)

