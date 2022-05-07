from ClaseNodo import Nodo

class ListaEnlazada:
    def __init__(self):
        """ Crea un objeto capaz de manejar nodos. No apunta a ningun nodo (self.prim = None) y no tiene elementos """
        self.prim = None
        self.len = 0
    def __iter__(self):
        """ Devuelve la lista como iterador.  Utiliza el método __next__ implementado en los nodos para pasar al setproximo elemento """
        self.iterador = self.prim
        if self.prim == None:
            raise StopIteration
        iter(self.iterador)
        return self.iterador
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
        self.len+=1
    def agregar_ordenado_asc(self,dato):
        """ Agrega elementos ordinales con orden ascendente """
        # Si la lista esta vacía, el nodo nuevo es el primero
        if self.estaVacia():
            nuevo = Nodo(dato)
            self.prim = nuevo
        else:
            nodoActual = self.prim
            # Sino, busco el primer nodo existente con un dato menor al propuesto
            while(nodoActual.proximo() != None and nodoActual.proximo().valor() < dato):
                nodoActual = nodoActual.proximo()
            if (nodoActual.proximo()==self.prim):
                nuevo = Nodo(dato,self.prim)
                self.prim = nuevo
            else:
                nuevo = Nodo(dato,nodoActual.proximo())
                nodoActual.setproximo(nuevo)
        print(nuevo.valor())
            
            

    
    
