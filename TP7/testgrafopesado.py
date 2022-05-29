from ClaseGrafoPond import Grafo
from ClaseRGrafo import BFS

gpes = Grafo()

gpes.insertar('TRV', 'EQS',peso_arco=21)
gpes.insertar('EQS', 'TCK',peso_arco=98)
gpes.insertar('TCK', 'GBC',peso_arco=100)
gpes.insertar('TCK', 'TRL',peso_arco=500)
gpes.insertar('GBC', 'CMD',peso_arco=300)
gpes.insertar('CMD', 'TRL',peso_arco=350)
gpes.insertar('TRL', 'RWS',peso_arco=25)
gpes.insertar('TRL', 'PMD',peso_arco=60)

gpes.imprimir_con_peso()


print(gpes)

