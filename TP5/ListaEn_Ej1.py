# Modificar el TAD ListaEnlazada visto en la teoría, de tal forma que:
# 1. No tenga la longitud de la lista en la cabecera (quitar el atributo len)
# 2. Tenga un atributo ult_nodo, que sea una referencia al último nodo de la lista. ¿Cuales son las ventajas y
# desventajas de agregar este atributo?
# 3. Tenga por lo menos los siguientes métodos: __str__ , __len__ , agregar(x), indice(x)
# Recordá modificar los métodos que se ven afectados por la desaparición/agregado de los atributos len y ult_nodo

# La ventaja de tener un puntero al útlimo elemento es que para devolver el mismo el orden de complejidad pasaría a ser
# constante, distinto a tener que recorrer la lista hasta encontrar el primer elemento que apunte a None, en ese caso el orden de
# complejidad es lineal

# Además de los métodos solicitados por el ejercicio, se añaden los métodos

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
            # Caso particular: saltear la cabecera de la lista
            nodoActual = self.prim
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (nodoAnterior)
            nodoAnterior = self.prim
            nodoActual = nodoAnterior.prox
            while nodoActual is not None and nodoActual.dato != x:
                nodoAnterior = nodoActual
                nodoActual = nodoAnterior.prox
            if nodoActual == None:
                raise ValueError("El valor no está en la lista.")
            # Descartar el nodo
            nodoAnterior.prox = nodoActual.prox
        # Si el elemento que se borró fue el último, actualizar self.ult_nodo
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
            # Caso particular: Saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            nodoAnterior = self.prim
            nodoActual = nodoAnterior.prox
            for pos in range(1, i):
                nodoAnterior = nodoActual
                nodoActual = nodoAnterior.prox
            # Guardar el dato y descartar el nodo
            dato = nodoActual.dato
            nodoAnterior.prox = nodoActual.prox
        # Si el elemento que se borró fue el último, actualizar self.ult_nodo
        if nodoAnterior.prox == None:
            self.ult_nodo = nodoAnterior
        print(self.ult_nodo.dato)
        return dato

    def ultimo(self): # Ya que estamos, agregamos un método para saber cual es el último nodo de la lista
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
