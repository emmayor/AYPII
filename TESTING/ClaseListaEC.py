class Nodo:
    def __init__(self, p_id, p_nm, p_tt, p_tr, prox=None):
        self.proc_id = p_id
        self.proc_nm = p_nm
        self.proc_tt = p_tt
        self.proc_tr = p_tr
        self.prox = prox
	
    def __str__(self):
        return str(self.proc_id)+"-"+self.proc_nm

    def actualizar(self, factor):
        self.proc_tr += factor

    def proceso(self):
        return self.proc_id
    
    def tiempoR(self):
        return self.proc_tr

    def tiempoT(self):
        return self.proc_tt
        
    def proximo(self):
        return self.prox

    def isHeader(self):
        return False

    def siguiente(self, unNodo):
        """ Engancha el nodo actual, self, con unNodo """
        self.prox = unNodo

class ListaEC:
    """Modela una lista enlazada."""

    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        self.ulti = None
        # cantidad de elementos de la lista
        self.len = 0

    def es_vacia(self):
        return self.len == 0

    def isHeader(self):
        return True

    def primero(self):
        return self.prim
        
    def append(self, p_id, p_nm, p_tt):
        # agrega un dato al final de la lista circular
        nuevoNodo = Nodo(p_id, p_nm, p_tt, p_tt, self)
        if self.es_vacia():
            self.prim = nuevoNodo
        else:
            #self.ulti.proximo() = nuevoNodo
            self.ulti.siguiente(nuevoNodo)
        self.ulti = nuevoNodo
        self.len += 1

    def remove(self, p_id):
        # devuelve el nodo que contiene a dato y lo quita de la lista
        if self.es_vacia():
            raise IndexError("El nodo no existe")
        actNodo = self.prim
        antNodo = None
        while (actNodo.proceso() != p_id and not actNodo.isHeader()):
            antNodo = actNodo
            actNodo = actNodo.proximo()

        if actNodo.isHeader():
            raise IndexError("El nodo no existe")

        if self.len == 1:
            self.prim = None
            self.ulti = None
        else:
            antNodo.siguiente(actNodo.proximo())
        self.len -= 1
        return actNodo

    def removeB(self, nodo1, nodo2):
        # Remueve el nodo2 de la lista circular
        if nodo1 == None:
            # Borrar el primer nodo
            if nodo2 == self.prim:
                self.prim = nodo2.proximo()
            else:
                raise IndexError("Error de consistencia en la lista/en los nodos")
        
        elif nodo2 == self.ulti:
            # Borrar el último nodo
            nodo1.siguiente(nodo2.proximo())
            self.ulti = nodo1
        else:
            # Borrar un nodo "del medio"
            nodo1.siguiente(nodo2.proximo())
        self.len -= 1
        if self.len == 0:
            self.prim = None
            self.ulti = None

    def recorrer(self, cant):
        # Recorre la lista circular una cantidad cant de veces 
        if not self.es_vacia():
            nvuelta = 0
            actNodo = self.prim
            while nvuelta < cant:
                print(actNodo, end=" ")
                actNodo = actNodo.proximo()
                if actNodo.isHeader():
                    actNodo = self.prim
                    nvuelta += 1
                    print()

    def imprimir(self):
        if not self.es_vacia():
            actNodo = self.prim
            while not actNodo.isHeader():
                print(actNodo, end=" ")
                actNodo = actNodo.proximo()
