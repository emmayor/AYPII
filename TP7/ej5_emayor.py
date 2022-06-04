# Ejercicio 5
# Implementar un algoritmo que convierta un grafo representado con 
# matriz de adyacencia a un grafo representado con listas de adyacencia.

from tads.GrafoMat import GrafoMat
from tads.Grafo import Grafo

# CREACION DE GRAFO
grafoMat = GrafoMat()

# INSERCION DE NODOS
grafoMat.insertar('EQS','TRV')
grafoMat.insertar('TRW','RWS')
grafoMat.insertar('BRL','EQS')
grafoMat.insertar('EQS','PTM')
grafoMat.insertar('PTM','RWS')
grafoMat.insertar('BSA','RWS')

def convertirGrafoMatALista(grafoMat):
    grafoLE = Grafo()
    gmat_vertices = grafoMat.vertices()['V']
    gmat_arcos = grafoMat.vertices()['M']
    for x in range(grafoMat.n_vertices()):
        for y in range(grafoMat.n_vertices()):
            if gmat_arcos[x][y]:
                grafoLE.insertar(gmat_vertices[x],gmat_vertices[y])
    return grafoLE

grafoLE = convertirGrafoMatALista(grafoMat)
grafoLE.imprimir()





