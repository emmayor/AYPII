from ClaseNodo import Nodo

nombre = ''
puntero = None
nombre = input("Ingrese un nombre\n> ")

while nombre != '0':
    puntero = Nodo(nombre, puntero)
    nombre = input("Ingrese un nombre\n> ")
    
puntero.imprimirLista()



