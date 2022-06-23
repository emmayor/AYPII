# Podemos representar naturalmente las ciudades de un mapa caminero con un grafo, y hacer cálculos de
# distancia y selección de caminos, a partir de este grafo.
# Dado el plano de ciudades del noroeste del Chubut de la figura, y las dos tablas de distancias,
# (a) Usando el TAD grafo, cargar los datos correspondientes.
# (b) Ejecutar el algoritmo de Dijkstra del Ejercicio 7 e imprimir una tabla que muestre las distancias
# de Esquel a todas las otras ciudades o puntos del camino.
# (c) Escribir un programa que solicite una ciudad cualquiera e imprima las distancias hasta las
# otras ciudades o puntos del mapa.
# (d) Cómo se podría modificar el peso de los caminos, sin usar la distancia? O con algún dato que
# complementara la distancia entre ciudades?

from tads.GrafoPond import GrafoPond
from tads.Dijkstra import *

# Este es un comentario nuevo

ciudades = {
    "A":"Esquel",
    "B":"Trevelin",
    "C":"Cruce al Lago (con ruta 71)",
    "D":"Corcovado",
    "E":"Tecka",
    "F":"Puesto Leleque",
    "G":"Cholila",
    "H":"Cruce Los Retamos",
    "I":"Epuyén",
    "J":"El Maitén",
}

rutas = [
    ("A","B",24,True),
    ("A","C",24,True),
    ("A","E",97,True),
    ("A","F",94,True),
    ("B","C",15,True),
    ("B","D",64,True),
    ("C","G",95,True),
    ("D","E",75,True),
    ("F","G",37,True),
    ("F","H",27,True),
    ("F","J",39,True),
    ("G","H",30,True),
    ("H","I",7,True),
    ("I","J",39,True),
]

grafoComarca = GrafoPond()
for r in rutas:
    grafoComarca.insertar(ciudades[r[0]],ciudades[r[1]],r[2],r[3])

#grafoComarca.imprimir_con_peso()

print("Calculador de distancias entre localidades.")
print("Ingrese una de las siguientes localidades para conocer su distancia a las demás:")
for ciudad in ciudades:
    print(ciudades[ciudad])


inputCiudad = input("> ")

Dijkstra(grafoComarca,inputCiudad)



