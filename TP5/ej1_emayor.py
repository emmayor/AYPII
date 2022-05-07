from ListaEn_Ej1 import *

miLista = ListaEnlazada()

miLista.agregar_ordenado_asc("a")
miLista.agregar_ordenado_asc("b")
miLista.agregar_ordenado_asc("c")

print(miLista.ult_nodo.dato)

print(len(miLista))

print(miLista)
print(miLista.indice("a"))