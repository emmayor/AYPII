from ListaEn_def import ListaEnlazada, intercambiar

# Código de prueba
listaItems = ListaEnlazada()

listaItems.append('A')
listaItems.append('B')
listaItems.append('C')
listaItems.append('D')
listaItems.append('E')
listaItems.append('F')

print(listaItems)
intercambiar(3,listaItems)
print(listaItems)