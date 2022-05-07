# Modificar el TAD ListaEnlazada visto en la teoría, de tal forma que:
# 1. No tenga la longitud de la lista en la cabecera (quitar el atributo len)
# 2. Tenga un atributo ult_nodo, que sea una referencia al último nodo de la lista. ¿Cuales son las ventajas y
# desventajas de agregar este atributo?
# 3. Tenga por lo menos los siguientes métodos: __str__ , __len__ , agregar(x), indice(x)
# Recordá modificar los métodos que se ven afectados por la desaparición/agregado de los atributos len y ult_nodo

# La ventaja de tener un puntero al útlimo elemento es que para devolver el mismo el orden de complejidad pasaría a ser
# constante, distinto a tener que recorrer la lista hasta encontrar el primer elemento que apunte a None, cuyo orden de
# complejidad es lineal

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
        if self.estaVacia():
            return 0
        cuenta = 1
        nodoActual = self.prim
        while(nodoActual.proximo() != None):
            nodoActual = nodoActual.proximo()
            cuenta += 1
        return cuenta
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
        # Si la lista está vacía, o el elemento debería ir
        # primero, se crea el nodo apuntando a self.prim
        # (que podría valer None cuando está vacía)
        # y se lo convierte en primer nodo
        if self.estaVacia() or dato < self.prim.valor():
            nuevo = Nodo(dato,self.prim)
            self.prim = nuevo
        # En cualquier otro caso:
        else:

            # Se parte desde el primer nodo:
            nodoActual = self.prim

            # Se busca su posición comparando su valor con
            # el de nodoActual() hasta que llega a uno con mayor valor
            # o hasta que no hayan más (esto queriendo decir que debe ir último)
            while(nodoActual.proximo() != None and nodoActual.proximo().valor() < dato):
                nodoActual = nodoActual.proximo()

            # Luego se crea el nuevo apuntando al próximo de nodoActual...
            nuevo = Nodo(dato,nodoActual.proximo())

            # ...y por último se apunta el nodoActual al nuevo...
            nodoActual.setproximo(nuevo) # setproximo() = siguiente()

            # La asignación quedaría de la siguiente manera:
            # ... -> nodoActual -> nuevo -> nodoActual.proximo() -> ...
            # (obviamente que luego de ésta operación "nodoActual.proximo()" sería "nuevo",
            # pero es para dar una idea de cómo queda "encajado" entre los dos que ya estaban)

            # Si el elemento agregado es el último de la lista, entonces apuntamos
            # self.ult_nodo al elemento agregado
        if nuevo.proximo() == None:
            self.ult_nodo = nuevo