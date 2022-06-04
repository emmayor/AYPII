# Implementar un algoritmo que calcule el grado de entrada y el grado de 
# salida de un vértice. Calcular el orden de complejidad para cada uno de los 
# programas en el TAD que utiliza listas adyacentes y para el TAD
# que utiliza matrices de adyacencia.

# Grado de salida de un vértice:  es el número de aristas que empiezan en el vértice.
# Grado de entrada de un vértice: es el número de aristas que terminan en el vértice.

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

# CREACION DE GRAFO
grafoLE = Grafo()

# INSERCION DE NODOS
grafoLE.insertar('EQS','TRV')
grafoLE.insertar('TRW','RWS')
grafoLE.insertar('BRL','EQS')
grafoLE.insertar('EQS','PTM')
grafoLE.insertar('PTM','RWS')
grafoLE.insertar('BSA','RWS')

# Grado de complejidad: O(n)
def gradoSalidaMat(grafo, vertice):
    listaVertices = grafo.vertices()['V']
    matrizArcos = grafo.vertices()['M']
    salida = 0
    # Localizar el vértice
    indice = listaVertices.index(vertice)
    if indice != None:
        salida = sum(matrizArcos[indice]) 
    return salida

# Grado de complejidad: O(n)
def gradoEntradaMat(grafo, vertice):
    listaVertices = grafo.vertices()['V']
    matrizArcos = grafo.vertices()['M']
    entrada = 0
    # Localizar el vértice
    indice = listaVertices.index(vertice)
    if indice != None:
        for v in range(grafo.n_vertices()):
            if matrizArcos[v][indice]:
                entrada += 1
    return entrada

# Grado de complejidad: O(n)
def gradoSalidaLE(grafo, vertice):
    salida = 0
    primNodo = grafo.vertices()[vertice]
    while primNodo != None:
        salida+=1
        primNodo = primNodo.proximo()
    return salida


# Grado de complejidad: O(n^2)
def gradoEntradaLE(grafo, vertice):
    entrada = 0
    for v in grafo.vertices():
        primNodo = grafo.vertices()[v]
        while primNodo != None:
            if primNodo.dato == vertice:
                entrada+=1
            primNodo = primNodo.proximo()
    return entrada

salidaMat = gradoSalidaMat(grafoMat, 'EQS')
entradaMat = gradoEntradaMat(grafoMat, 'RWS')
salidaLE = gradoSalidaLE(grafoLE, 'EQS')
entradaLE = gradoEntradaLE(grafoLE, 'RWS')

print("Matriz de adyacencia: ")
print(f"SALIDA: {salidaMat}")
print(f"ENTRADA: {entradaMat}")

print("Lista de adyacencia: ")
print(f"SALIDA: {salidaLE}")
print(f"ENTRADA: {entradaLE}")



    

        
