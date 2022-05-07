""" Escribí un método iguales(). Dos listas enlazadas se consideran iguales si contienen los mismos nodos (no el
mismo objeto nodo, sino nodos con los mismos datos), en el mismo orden. Utilizá el siguiente algoritmo:
1. Comparar el tamaño de las dos listas, si no tienen la misma longitud, es imposible que sean iguales.
2. Si las listas son de la misma longitud, comparar cada nodo de una lista con el de la misma posición
relativa de la otra lista.
3. Si cualquiera de los nodos es diferente, este método debe devolver “False”.
4. Si se terminó de chequear todos los nodos y todos son iguales, el método debe devolver “True”."""

from ClaseNodo import Nodo

class ListaEnlazada:
    def __init__(self):
        """ Crea un objeto capaz de manejar nodos. No apunta a ningun nodo (self.prim = None) y no tiene elementos """
        self.prim = None
        self.ult_nodo = None

    def __iter__(self):
        """ Devuelve la lista como iterador.  Utiliza el método __next__ implementado en los nodos para pasar al setproximo elemento """
        self.iterador = self.prim
        if self.prim == None:
            raise StopIteration
        iter(self.iterador)
        return self.iterador

    def __len__(self):
        """ Devuelve la longitud de la lista """
        if self.estaVacia():
            return 0
        cuenta = 1
        nodoActual = self.prim
        while(nodoActual.proximo() != None):
            nodoActual = nodoActual.proximo()
            cuenta += 1
        return cuenta

    def __str__(self):
        """ Devuelve la lista como string, separando los elementos entre espacios"""
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
            nodoActual.setproximo(nuevo) # setproximo() = siguiente()
        if nuevo.proximo() == None:
            self.ult_nodo = nuevo

    def indice(self,busqueda):
        """ Devuelve el índice de un elemento. Si no se encuentra, devuelve None"""
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
        
    def imprimir(self):
        """ Imprime la lista en formato de listas de Python """
        if self.estaVacia():
            print('[]', end="")
        else:
            nodoActual = self.prim
            print('[', end="")
            while(nodoActual != None):
                print(nodoActual.valor(), end="")
                if nodoActual.proximo() != None:
                    print(', ', end="")
                nodoActual = nodoActual.proximo()
            print(']')

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