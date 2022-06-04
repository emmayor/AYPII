from tads.Cola import Cola

def procesar_vertice_temprano(valor_vertice):
	print(f"Vertice: {valor_vertice}")
	
def procesar_arista(valx, valy):
	print(f"Arista({valx}, {valy})")
	
def procesar_vertice_tarde(valor_vertice):
	return None

def BFS(G, s):
	estado = {}		# Estado de los Vértices
	padre = {}		# Vértices con sus padres
	vertices = G.vertices()
	q = Cola()
					# Seteo inicial de V
	for ve in vertices:
		estado[ve]= "N"
		padre[ve] = None
					# Analizar V inicial
	estado[s] = "D"
	q.encolar(s)
	# Mientras hayan vértices que procesar
	while not q.estaVacia():
		u = q.desencolar()
		
		procesar_vertice_temprano(u)
		estado[u] = "P"
		adyacente = vertices[u]
		
		while adyacente: # Descubrir adyacentes!
			valor = adyacente.valor()
			if estado[valor] != "P" or G.dirigido():
				procesar_arista(u, valor)
			if estado[valor] == "N":
				q.encolar(valor)
				estado[valor] = "D"
				padre[valor] = u
				
			adyacente = adyacente.proximo()
		procesar_vertice_tarde(u)
		
		""" Devolver el diccionario de vertices con sus padres!!
		Para armar el árbol resultante """
	return padre

