def inicializar_v(vertices):
    """ Devuelve una lista c/los vértices sin descubrir """
    """ y en orden. Todos tienen False en el estado """
    visitados = []
    for ve in sorted(vertices.items()):
        elem = list(ve)
        elem[1] = False     # Todos sin descubrir!
        visitados.append(elem)
    return visitados

def set_mark(visitados, ve, valor):
    """ Pone el valor del vértice ve en visitado, ve existe """
    i = 0                   # Encontrar el vértice ve
    while (i < len(visitados) and visitados[i][0]!=ve):
        i+=1 
    visitados[i][1] = valor # Modificar

def Dijkstra(G, s):
    """ Calcula el menor camino desde s a todos los vértices de G """
    
    """ Inicializar el diccionario de distancias """
    distancia = {}
    vertices = G.vertices()
    for ve in vertices:
        distancia[ve] = float("inf")        # infinito en Python

    """ Listado de los vértices (ORDENADOS) con visitado = False """
    visitados = inicializar_v(vertices)

    distancia[s] = 0
    while quedan_sin_descubrir(visitados):

        v = minVert(G, distancia, visitados)# encontrar el próximo mas cercano
        #print("Ver:", v)
        set_mark(visitados, v, True)
        if distancia[v] == float("inf"):    # vertice inalcanzable
            print("Componente no conexa: ", v)
        else:
            arista = G.primer_adyacente(v)
            #print("primer adyacente: ", arista)
            while arista:
                w = arista.valor()          # devuelve el veŕtice          
                if (distancia[w] > (distancia[v] + arista.peso())):
                    distancia[w] = distancia[v] + arista.peso()
                    print(f"d({v},{w}) = {distancia[w]}")
                arista = arista.proximo()       
    return distancia
        
def minVert(G, dist, visit):
    """ Encuentra el menor de los no visitados """
    """ Recibe el grafo, el dicc de distancias y la lista de visitados"""

    i = 0                   
    while i < len(visit) and visit[i][1]:
        i +=1               # Iterar hasta encontrar el primer falso
    if i < len(visit):
        v = visit[i][0]     # Encontré uno sin visitar. Es el mínimo?
        for i in range(i+1,len(visit)):
            if (visit[i][1] == False and dist[visit[i][0]] < dist[v]):
                v = visit[i][0]    # Hay otro menor
    else:
        v = None        # Puede ser que no haya ninguno?   
    return v

def quedan_sin_descubrir(visitados):
    """ Devuelve True/False según queden vértices sin visitar """
    indice = 0
    while indice < len(visitados) and visitados[indice][1]:
        indice +=1
    return (indice < len(visitados) and (not visitados[indice][1]))
