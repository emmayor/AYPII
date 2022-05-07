class Nodo:
    def __init__(self,dato=None,prox=None):
        """Crea un nodo con un valor y un puntero al próximo nodo"""
        self.dato = dato
        self.prox = prox
    def __iter__(self):
        """ Devuelve un nodo como iterable """
        self.iterador = self
        return self.iterador
    def __next__(self):
        """ Devuelve el siguiente nodo cuando se invoca como iterable """
        siguiente = self.iterador
        if siguiente == None:
            raise StopIteration
        self.iterador = siguiente.proximo()
        return siguiente
    def __str__(self):
        return str(self.dato)
    def imprimirLista(self):
        """ Imprime desde éste elemento hasta el último que esté enlazado """
        while self != None: 
            print(self)
            self = self.prox
    def imprimirInversa(self):
        """ Imprime desde el último enlazado hasta este elemento """
        if self.prox != None:
            self.prox.imprimirInversa(self.prox)
        print(self)
    def valor(self):
        """ Devuelve el valor del nodo """
        return self.dato
    def proximo(self):
        """ Devuelve el próximo elemento a éste """
        return self.prox
    def setproximo(self, otro):
        """ Establece el próximo elemento a éste """
        self.prox = otro

        

