# Modificar el TAD ListaEnlazada visto en la teoría, de tal forma que:
# 1. No tenga la longitud de la lista en la cabecera (quitar el atributo len)
# 2. Tenga un atributo ult_nodo, que sea una referencia al último nodo de la lista. ¿Cuales son las ventajas y
# desventajas de agregar este atributo?
# 3. Tenga por lo menos los siguientes métodos: __str__ , __len__ , agregar(x), indice(x)
# Recordá modificar los métodos que se ven afectados por la desaparición/agregado de los atributos len y ult_nodo

# La ventaja de tener un puntero al útlimo elemento es que para devolver el mismo el orden de complejidad pasaría a ser
# constante, distinto a tener que recorrer la lista hasta encontrar el primer elemento que apunte a None, cuyo orden de
# complejidad es lineal

from ClaseLista import ListaEnlazada

miLista = ListaEnlazada()

miLista.agregar_ordenado_asc("a")
miLista.agregar_ordenado_asc("b")
miLista.agregar_ordenado_asc("c")

print(miLista.ult_nodo.dato)

print(len(miLista))

print(miLista)
print(miLista.indice("a"))