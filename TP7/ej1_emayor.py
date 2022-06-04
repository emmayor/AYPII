# Implementar la clase grafo, utilizando matrices de adyacencia, con los mismos métodos que se incluyeron
# para la implementación con listas de adyacencia.

from tads.GrafoMat import GrafoMat
# from tads.GrafoMat import plotGrafo

# CREACION DE GRAFO
grafo1 = GrafoMat()

# INSERCION DE NODOS
grafo1.insertar('EQS','TRV',True)
grafo1.insertar('TRW','RWS')
grafo1.insertar('BRL','EQS',True)
grafo1.insertar('VDM','PTM',True)
grafo1.insertar('PTM','RWS')

# IMPRESION DE GRAFO
grafo1.imprimir()

# IMPRESION DE CANTIDADES
print(grafo1)

# plotGrafo(grafo1)