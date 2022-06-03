from tads.GrafoMat import plotGrafo
from tads.GrafoMat import GrafoMat

grafo1 = GrafoMat()
grafo1.insertar('EQS','TRV',True)
grafo1.insertar('TCK','TRW')
grafo1.insertar('EQS','BRL',True)
grafo1.insertar('TRW','RWS')

plotGrafo(grafo1)