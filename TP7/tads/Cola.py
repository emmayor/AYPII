class Cola:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        if len(self.items) == 0:
            return True
        return False
    
    def encolar(self, elemento):
        return self.items.append(elemento)
    
    def desencolar(self):
        if self.estaVacia():
            raise IndexError("La cola esta vacía")
        return self.items.pop(0)

    def __str__(self):
        return str(self.items)  

class ColaExt:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        if len(self.items) == 0:
            return True
        return False
    
    def encolar(self, elemento):
        return self.items.append(elemento)
    
    def desencolar(self):
        if self.estaVacia():
            raise IndexError("La cola esta vacía")
        return self.items.pop(0)

    def espejo(self):
        resultado = ""
        colaAux = Cola() # 3
        while not self.estaVacia(): # Se procesa el contenido de la cola, se realizan n iteraciones para 4 instrucciones: 4n
            lAux = self.sacar() 
            colaAux.apilar(lAux)
            resultado += lAux
        while not colaAux.estaVacia(): # Se añade el contenido invertido de la pila a una variable auxiliar, se realizan n iteraciones para 4 instrucciones: 4n
            resultado += colaAux.desapilar()
        for i in resultado: # Se vuelve a meter en la cola el contenido en su orden original y en su orden inverso, se realizan 2n iteraciones para 2 instrucciones: 4n
            self.meter(i)
        return self # 1
        # Compliejidad: 12n + 4 = O(n)

    def __str__(self):
        return str(self.items)  
