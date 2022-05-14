# Implemente, usando el TAD Árbol, un programa que arme el árbol 
# genealógico de una persona, partiendo de esa
# persona (raíz) y preguntando quién es su madre/padre. 
# Deberá terminar con una persona cuando la respuesta, en
# cada caso, sea “no sé”. Una vez cargado el árbol, imprímalo. 
# Puede usar el módulo que imprime árboles
# gráficamente, con las adaptaciones necesarias para que “entren” los nombres.

from ArbolBB import ArbolBB

# PAPA = IZQUIERDO, MAMA = DERECHO

def imprimirArbol(arbol,nivel=0):
    print(arbol.valor())
    nivel += 1
    if arbol.subizq() != None:
        print("├"+"────"*nivel,end="")
        imprimirArbol(arbol.subizq(),nivel)
    if arbol.subder() != None:
        print("├"+"────"*nivel,end="")
        imprimirArbol(arbol.subder(),nivel)

def agregarPadres(arbol, nombre):
    print(f"PERSONA ACTUAL: {nombre}")
    padre = input(f"Ingrese el nombre del padre de {nombre} (\"no sé\" para omitir)\n> ")
    madre = input(f"Ingrese el nombre de la madre de {nombre} (\"no sé\" para omitir)\n> ")
    if padre != "no sé":
        arbol.izquierdo(padre)
        agregarPadres(arbol.subizq(),padre)
    if madre != "no sé":
        arbol.derecho(madre)
        agregarPadres(arbol.subder(),madre)
    return
    
entrada = input("Ingrese el nombre de la persona raíz.\n> ")
arbol = ArbolBB(entrada)
agregarPadres(arbol,entrada)
imprimirArbol(arbol)



      