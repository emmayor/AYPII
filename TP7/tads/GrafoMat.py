import matplotlib.pyplot as plt

class GrafoMat:
    """ Crea un grafo. Las relaciones se representan con una matriz de adyacencia. Si es_dirigido se establece en True, 
    todos los nodos que se inserten tendran aristas simples por defecto y aristas dobles en caso contrario"""
    def __init__(self, es_dirigido=False):
        self.lista_vertices = []
        self.mat = []
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

    def insertarArco(self, ix, iz):
        self.mat[ix][iz] = True
        self.n_arcos+=1
        
    def insertar(self, x, z, doble=False):
        if x not in self.lista_vertices:
            self.lista_vertices.append(x)
            for i in self.mat:
                i.append(False)
            self.mat.append([False for i in range(self.n_vertices())])
        if z not in self.lista_vertices:
            self.lista_vertices.append(z)
            for i in self.mat:
                i.append(False)
            self.mat.append([False for i in range(self.n_vertices())])      
        ix = self.lista_vertices.index(x)
        iz = self.lista_vertices.index(z)
        self.insertarArco(ix,iz)
        if doble:
            self.insertarArco(iz,ix)

    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print("->", end=' ')
                arco.imprimirLista()
            print("")


def plotGrafo(grafo):
    nvalues = range(grafo.n_vertices())
    plt.matshow(grafo.mat)
    plt.xticks(nvalues,grafo.lista_vertices)
    plt.yticks(nvalues,grafo.lista_vertices)
    plt.show()
        
            

