from Nodo import Nodo

class Grafo:
    """ Crea un grafo. Si es_dirigido se establece en True, 
    todos los nodos que se inserten tendran aristas simples por defecto y aristas dobles en caso contrario"""
    def __init__(self, es_dirigido=False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido

    def __str__(self):
        return "G = ("+str(self.n_vertices())+" V, "+str(self.n_arcos)+" A)"

    def n_vertices(self):
        return len(self.lista_vertices)

    def dirigido(self):
        return self.es_dirigido

    def vertices(self):
        return self.lista_vertices

    def n_arcos(self):
        return self.n_arcos

    def primer_adyacente(self, x):
        """ Devuelve el primer vértice adyacente (si existe) de x"""
        if x not in self.lista_vertices:
            raise ValueError("El vértice no existe en el diccionario del Grafo")
        else:
            return self.lista_vertices[x]

    def insertarArco(self,x,z):
        """Se carga el arco. ATENCION: Deben existir los vertices previamente"""
        nw = Nodo(z, self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos += 1

    def insertar(self, x, z, doble=False):
        if x not in self.lista_vertices:
            self.lista_vertices[x] = None
        """ Agregar el destino (ojo, x sumideros)"""
        if z not in self.lista_vertices:
            self.lista_vertices[z] = None
        self.insertarArco(x, z)
        if (doble) and z != x:
            self.insertarArco(z, x)

    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print("->", end=' ')
                arco.imprimirLista()
            print("")


           
            
