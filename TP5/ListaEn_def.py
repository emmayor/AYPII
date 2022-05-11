from ClaseNodo import Nodo

class ListaEnlazada:
    def __init__(self):
        """ Crea un objeto capaz de manejar nodos. No apunta a ningun nodo (self.prim = None) y no tiene elementos """
        self.prim = None
        self.ult_nodo = None
    def __iter__(self):
        """ Devuelve la lista como iterador. Utiliza el método __next__ implementado en los nodos para pasar al setproximo elemento """
        self.iterador = self.prim
        if self.prim == None:
            raise StopIteration
        iter(self.iterador)
        return self.iterador
    def __len__(self):
        """ Devuelve la longitud de la lista recorriendola """
        if self.estaVacia():
            return 0
        cuenta = 1
        nodoActual = self.prim
        while(nodoActual.proximo() != None):
            nodoActual = nodoActual.proximo()
            cuenta += 1
        return cuenta
    def imprimir(self):
        if self.estaVacia():
            print('[]')
        else:
            nodoActual = self.prim
            print('[', end="")
            while(nodoActual != None):
                print(nodoActual.valor(), end="")
                if nodoActual.proximo() != None:
                    print(', ', end="")
                nodoActual = nodoActual.proximo()
            print(']')
    def indice(self,busqueda):
        """ Devuelve la posición del nodo buscado """
        if self.estaVacia():
            return None
        indice = 0
        nodoActual = self.prim
        while(nodoActual != None and nodoActual.dato != busqueda):
            nodoActual = nodoActual.proximo()
            indice += 1
        if nodoActual == None:
            return None
        return indice
    def borrar(self,x): 
        if self.estaVacia():
            raise ValueError("Lista Vacía.")
        if self.prim.dato == x:
            nodoActual = self.prim
            self.prim = self.prim.prox
        else:
            nodoAnterior = self.prim
            nodoActual = nodoAnterior.prox
            while nodoActual is not None and nodoActual.dato != x:
                nodoAnterior = nodoActual
                nodoActual = nodoAnterior.prox
            if nodoActual == None:
                raise ValueError("El valor no está en la lista.")
            nodoAnterior.prox = nodoActual.prox
            if nodoActual.prox == None:
                self.ult_nodo = nodoAnterior
            print(self.ult_nodo.dato)
    def devolver(self, i=None):
        """ Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            nodoAnterior = self.prim
            nodoActual = nodoAnterior.prox
            for pos in range(1, i):
                nodoAnterior = nodoActual
                nodoActual = nodoAnterior.prox
            dato = nodoActual.dato
            nodoAnterior.prox = nodoActual.prox
        if nodoAnterior.prox == None:
            self.ult_nodo = nodoAnterior
        print(self.ult_nodo.dato)
        return dato
    def ultimo(self): 
        return self.ult_nodo
    def __str__(self):
        text = ""
        nodo = self.prim
        while (nodo!=None):
            text += str(nodo)+" "
            nodo = nodo.proximo()
        return text 
    def estaVacia(self):
        """ Devuelve True si la lista está vacía, False en caso contrario """
        if self.prim == None:
            return True
        return False
    def append(self,dato):
        """ Agrega un nuevo elemento al final de la lista """
        nuevoNodo = Nodo(dato)
        if self.prim == None:
            self.prim = nuevoNodo
        else:
            n = self.prim
            while n.proximo()!=None:
                n = n.proximo()
            n.setproximo(nuevoNodo)
        self.ult_nodo = nuevoNodo
    
    def agregar_ordenado_asc(self,dato):
        """ Agrega elementos con orden ascendente """
        if self.estaVacia() or dato < self.prim.valor():
            nuevo = Nodo(dato,self.prim)
            self.prim = nuevo
        else:
            nodoActual = self.prim
            while(nodoActual.proximo() != None and nodoActual.proximo().valor() < dato):
                nodoActual = nodoActual.proximo()
            nuevo = Nodo(dato,nodoActual.proximo())
            nodoActual.setproximo(nuevo) 
        if nuevo.proximo() == None:
            self.ult_nodo = nuevo
    def iguales(self, otraLista):
        """ Compara dos listas: La que llama al método y la que se pasa por parámetro. 
        Si son iguales devuelve True, en caso contrario devuelve False"""
        if len(self) != len(otraLista):
            return False
        nodoActual = self.prim
        otraActual = otraLista.prim
        while (nodoActual != None):
            if nodoActual.valor() != otraActual.valor():
                return False
            nodoActual = nodoActual.proximo()
            otraActual = otraActual.proximo()
        return True

def intercambiar(i, lista):
    """ Invierte la posicion del i-elemento de la lista con su siguiente
     (i va de 0 a hasta len-1)"""
    ant = lista.prim
    act = ant.proximo()
    sig = act.proximo()
    if i == 0:
        ant.setproximo(sig)
        act.setproximo(lista.prim)
        ant = act
    elif i > 0 and i < len(lista)-1:
        for i in range(i-1):
            ant = ant.proximo()               
        act = ant.proximo()
        sig = act.proximo()

        ant.setproximo(sig)
        act.setproximo(sig.proximo())
        sig.setproximo(act)
    else:
        raise IndexError("Item fuera de rango")

        
def intercalarDesc(lista1, lista2):
    listaFinal = ListaEnlazada()
    # Buscamos la lista más larga
    lenMin,lenMax = sorted([len(lista1), len(lista2)])
    if lenMax == len(lista1):
        larga = lista1
    else:
        larga = lista2
    lenMod = lenMax - lenMin
    # Esto no me gusta para nada, pero no concibo cómo
    # iterar la lista al reves sin modificar el TAD!
    # ListaEnlazada -> Iterable -> Lista -> ListaInvertida
    listaTemp = reversed(list(larga))
    # Primero sumamos los elementos extra de la lista mas larga
    while lenMod > 0:
        listaFinal.append(next(listaTemp))
        lenMod-=1
    # Despues intercalamos con el resto y los preordenamos para 
    # agregarlos a la lista final
    for item1,item2 in reversed(list(zip(lista1,lista2))):
        mini,maxi = sorted([item1.valor(), item2.valor()])
        listaFinal.append(maxi)
        listaFinal.append(mini)
    return listaFinal
