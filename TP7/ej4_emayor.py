# Ejercicio 4
# Listar los vértices de un grafo que tienen grado de salida 0. 
# Estos vértices se llaman sumideros.
# Listar los vértices del grafo que tienen grado de entrada 0. 
# ¿Puede hacer algún comentario respecto a estos vértices?



from tads.Grafo import Grafo

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

def listarSumiderosLE(grafo):
    for v in grafo.vertices():
        if gradoEntradaLE(grafo, v) == 0:
            print(v)

def listarEntrada0LE(grafo):
    for v in grafo.vertices():
        if gradoSalidaLE(grafo, v) == 0:
            print(v)


# CREACION DE GRAFO
grafoLE = Grafo()

# INSERCION DE NODOS
grafoLE.insertar('EQS','TRV',True)
grafoLE.insertar('TRW','RWS')
grafoLE.insertar('BRL','EQS')
grafoLE.insertar('EQS','PTM')
grafoLE.insertar('PTM','RWS')
grafoLE.insertar('BSA','RWS')

print("Vértices con grado de entrada 0")
listarSumiderosLE(grafoLE)
print("Vértices con grado de salida 0")
listarEntrada0LE(grafoLE) 

