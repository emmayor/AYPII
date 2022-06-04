# Implementar el método TopSort visto en clase en alguno de los TAD implementados para grafos (con lista de
# adyacencia o con matriz de adyacencia).
# Luego, escribir un programa que cargue los datos correspondientes al plan de estudios de la carrera APU y
# ejecute el método TopSort. El orden resultante del algoritmo, ¿es similar al estado de sus cursadas? ¿Hay
# alguna forma de variar el orden del resultado, según la carga de los datos?

# El orden del resultado depende del orden en el que se carguen los elementos
# Son válidos, pero no son iguales


from tads.Grafo import *
from tads.Cola import Cola

def procesar_vertice_temprano(valor_vertice):
    print("Vértice ", valor_vertice)

def TopSortQ(G):

    q_vert = Cola()
    cuenta = {}
  
    """ Inicializar el diccionario de requisitos """
    vertices = G.vertices()
    for ve in vertices:
        cuenta[ve]= 0

    """ Recorro todos los vértices del grafo,
    para procesar las aristas """
    for ve in vertices:
        adyacente = G.primer_adyacente(ve)
        while adyacente:
            valor = adyacente.valor()
            cuenta[valor] += 1
            adyacente = adyacente.proximo()        

    for ve in cuenta:
        if cuenta[ve] == 0:
            """ ve no tiene requisitos, se puede procesar """
            q_vert.encolar(ve)
            
    while not q_vert.estaVacia():
        ve = q_vert.desencolar()
        procesar_vertice_temprano(ve)
        
        adyacente = G.primer_adyacente(ve)
        while adyacente:
            valor = adyacente.valor()
            cuenta[valor] -= 1
            if cuenta[valor] == 0:
                """ el vértice fue liberado """
                q_vert.encolar(valor)
            
            adyacente = adyacente.proximo()


materias = {
    "IF001":"Elementos de Informatica",
    "MA045":"Algebra",
    "IF002":"Expresión de Problemas y Algoritmos",
    "IF003":"Algorítmica y Programación I",
    "MA046":"Análisis Matemático",
    "MA008":"Elementos de Lógica y Matemática Discreta",

    "IF004":"Sistemas y Organizaciones",
    "IF005":"Arquitectura de Computadoras",
    "IF006":"Algorítmica y Programación II",
    "IF007":"Bases de Datos I",
    "MA006":"Estadística",
    "IF008":"Programación Orientada a Objetos",

    "IF009":"Laboratorio de Programación y Lenguajes",
    "IF010":"Análisis y Diseño de Sistemas",
    "IF011":"Sistemas Operativos",
    "IF012":"Desarrollo de Software",

    "FA007":"Acreditación de Idioma Inglés",
    "FA102":"(Curso) Estrategias Comunicacionales",
}

grafoAPU = Grafo()

grafoAPU.insertar(materias["IF001"], materias["IF005"]) # Elementos de Informatica -> Arquitectura de Computadoras
grafoAPU.insertar(materias["IF006"], materias["IF011"]) # Algorítmica y Programación II -> Sistemas Operativos
grafoAPU.insertar(materias["IF010"], materias["IF012"]) # Análisis y Diseño de Sistemas -> Desarrollo de Software
grafoAPU.insertar(materias["IF002"], materias["IF003"]) # Expresión de Problemas y Algoritmos -> Algorítmica y Programación I
grafoAPU.insertar(materias["IF003"], materias["IF006"]) # Algorítmica y Programación I -> Algoritmica y Programacion II
grafoAPU.insertar(materias["MA046"], materias["MA006"]) # Análisis Matemático -> Estadística
grafoAPU.insertar(materias["MA008"], materias["IF006"]) # Elementos de Lógica y Matemática Discreta -> Algoritmica y Programacion II
grafoAPU.insertar(materias["IF004"], materias["IF010"]) # Sistemas y Organizaciones -> Análisis y Diseño de Sistemas
grafoAPU.insertar(materias["IF005"], materias["IF011"]) # Arquitectura de Computadoras -> Sistemas Operativos
grafoAPU.insertar(materias["IF006"], materias["IF007"]) # Algorítmica y Programación II -> Bases de Datos I
grafoAPU.insertar(materias["IF006"], materias["IF008"]) # Algorítmica y Programación II -> Programación Orientada a Objetos
grafoAPU.insertar(materias["IF007"], materias["IF010"]) # Bases de Datos I -> Análisis y Diseño de Sistemas
grafoAPU.insertar(materias["IF008"], materias["IF009"]) # Programación Orientada a Objetos -> Laboratorio de Programación y Lenguajes
grafoAPU.insertar(materias["IF008"], materias["IF012"]) # Programación Orientada a Objetos -> Desarrollo de Software
grafoAPU.insertar(materias["MA045"], materias["MA006"]) # Algebra -> Estadística
grafoAPU.insertar(materias["FA007"], None)              # Acreditación de Idioma Inglés 
grafoAPU.insertar(materias["FA102"], None)              # (Curso) Estrategias Comunicacionales

TopSortQ(grafoAPU)








