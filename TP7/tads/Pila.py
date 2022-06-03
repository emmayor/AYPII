class Pila:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        if len(self.items) == 0:
            return True
        return False
    
    def apilar(self, elemento):
        return self.items.append(elemento)
    
    def desapilar(self):
        if self.estaVacia():
            raise IndexError("La pila esta vacía")
        return self.items.pop()
    def __str__(self):
        return str(self.items)

class PilaExt:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        if len(self.items) == 0:
            return True
        return False
    
    def apilar(self, elemento):
        return self.items.append(elemento)
    
    def desapilar(self):
        if self.estaVacia():
            raise IndexError("La pila esta vacía")
        return self.items.pop()

    def __str__(self):
        return str(self.items)

    def tope(self):
        if self.estaVacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]
