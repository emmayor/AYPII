from ..tads.GrafoPond import Grafo
from ..tads.GrafoPond import BFS


grafo1 = Grafo() 

a,b,c,d,e = "a","b","c","d","e"

grafo1.insertar(a, b, True)
grafo1.insertar(b,c)
grafo1.insertar(b,d)
grafo1.insertar(d,e)
grafo1.insertar(d,a)

grafo1.imprimir()
res = BFS(grafo1, "a")

