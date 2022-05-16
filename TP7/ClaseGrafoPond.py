class Arista:
	def __init__(self, dato=None, peso_arco=0, prox=None):
		self.dato = dato
		self.peso_arco = peso_arco
		self.prox = prox
	def __str__(self):
		return str(self.dato)
	def valor(self):
		return self.dato
	def proximo(self):
		return self.prox
	def peso(self):
		return self.peso_arco
	def imprimeLista(nodo):
		"""Recorre todos los nodos a través de sus enlaces,
		mostrando sus contenidos."""
		while nodo:
			print(nodo, end=" "),
			nodo = nodo.prox
		print(" ")
	def imprime_lista_con_peso(nodo):
		while nodo:
			print(nodo, "("+str(nodo.peso())+")",end=" "),
			nodo = nodo.prox
		print(" ")


class Grafo:
	def __init__(self, es_dirigido = False):
		self.lista_vertices = {}
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

	def insertar(self, x, z, peso_arco = 0, dirigido = False):
		""" Agregar el vértice de origen """
		if x not in self.lista_vertices:
			self.lista_vertices[x]= None
		""" Agregar el destino (ojo, x sumideros)"""
		if z not in self.lista_vertices:
			self.lista_vertices[z]= None
		
		nw = Arista(z, peso_arco, self.lista_vertices[x])
		self.lista_vertices[x] = nw
		self.n_arcos+=1
		if dirigido is False and z != x:
			self.insertar(z,x, peso_arco, True)
	def primer_adyacente(self, x):
		""" Devuelve el primer vértice adyacente (si existe) de x"""
		if x not in self.lista_vertices:
			raise Error("El vértice no existe en el diccionario del Grafo")
		else:
			return self.lista_vertices[x]

	def imprimir(self):
		for vertice in self.lista_vertices:
			print(vertice, end=' ')
			arco = self.lista_vertices[vertice]
			if arco is not None:
				print("->", end=' ')
				arco.imprimeLista()
			else:
				print("")
	def imprimir_con_peso(self):
		for vertice in self.lista_vertices:
			print(vertice, end=' ')
			arco = self.lista_vertices[vertice]
			if arco is not None:
				print("->", end=' ')
				arco.imprime_lista_con_peso()
			else:
				print("")
