from ListaEn_Ej1 import ListaEnlazada

def intercambiar(i, lista):
    """ Invierte la posicion del i-elemento de la lista con su siguiente (i va de 0 a hasta len-1)"""
    # Fijamos un elemento contiguo a otro
    ant = lista.prim
    act = ant.proximo()
    sig = act.proximo()

    # Si el índice es 0 (el primer elemento de la lista), entonces no hace falta referenciar al anterior
    # Simplemente se establece el próximo como el primer elemento y a éste último como el que le sigue

    if i == 0:
        lista.prim.setproximo(sig)
        act.setproximo(lista.prim)
        lista.prim = act

    # Si el índice está entre 0 y len-1, entonces buscamos el item moviendo de lugar
    # los tres punteros ant, act y sig

    elif i > 0 and i < len(lista)-1:
        for i in range(0, i-1):
            ant = ant.proximo()
            act = act.proximo()
            sig = sig.proximo()

        # Reasignamos los proximos de cada nodo
        ant.setproximo(sig)
        act.setproximo(sig.proximo())
        sig.setproximo(act)
    # En cualquier otro caso, el índice está fuera de rango
    else:
        raise IndexError("Item fuera de rango")




# Código de prueba

# listaItems = ListaEnlazada()

# listaItems.append('A')
# listaItems.append('B')
# listaItems.append('C')
# listaItems.append('D')
# listaItems.append('E')
# listaItems.append('F')
# listaItems.append('G')
# listaItems.append('H')
# listaItems.append('I')
# listaItems.append('J')

# print(listaItems)

# intercambiar(6,listaItems)

# print(listaItems)