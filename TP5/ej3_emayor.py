# Escribí un método iguales(). Dos listas enlazadas se consideran iguales si contienen los mismos nodos (no el
# mismo objeto nodo, sino nodos con los mismos datos), en el mismo orden. Utilizá el siguiente algoritmo:
# 1. Comparar el tamaño de las dos listas, si no tienen la misma longitud, es imposible que sean iguales.
# 2. Si las listas son de la misma longitud, comparar cada nodo de una lista con el de la misma posición
# relativa de la otra lista.
# 3. Si cualquiera de los nodos es diferente, este método debe devolver “False”.
# 4. Si se terminó de chequear todos los nodos y todos son iguales, el método debe devolver “True”.

from ClaseLista import ListaEnlazada

miLista = ListaEnlazada()

miLista.append("3")
miLista.append("trkjh")
miLista.append("865")

otraLista = ListaEnlazada()

otraLista.append("3")
otraLista.append("trkjh")
otraLista.append("865")





print(miLista.iguales(otraLista))
