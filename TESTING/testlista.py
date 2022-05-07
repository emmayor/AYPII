from ListaEn import ListaEnlazada

listaOrd = ListaEnlazada()
listaOrd.agregar_ordenado_asc('Matias')
listaOrd.agregar_ordenado_asc('Walter')
listaOrd.agregar_ordenado_asc('Lucas')
listaOrd.agregar_ordenado_asc('Emmanuel')
listaOrd.agregar_ordenado_asc('Santi')
listaOrd.agregar_ordenado_asc('Ivan')

for i in listaOrd:
    print(i)



