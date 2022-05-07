lista = list()
palabra = ""

# Se calcula la cantidad de elementos, se ordena la lista y 
# se devuelven el elemento del primer índice y del último
def primerUlt(lista):
    long = len(lista)
    lista.sort()
    return (lista[0],lista[long-1])

# Mientras el usuario no ingrese '0', el programa admitirá la 
# entrada de una cantidad indefinida de elementos
while palabra != '0':
    palabra = input("Ingrese una palabra. Ingrese 0 para continuar\n> ")
    if palabra != '0':
        lista.append(palabra)

# Se obtiene el resultado y se imprime
resultado = primerUlt(lista)
print(f"Primera y última palabra: {resultado}")
    