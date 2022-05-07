lista = ["Daniel", "Juan", "David", "Jorge", "Martin", "Marcos"]
letra = ""

def buscarNombre(lista,letra):
    resultado = list()
    long = len(lista)
    for i in lista:
        if letra in i[0]:
            resultado.append(i)
    return resultado

# Mientras el usuario no ingrese '0', el programa admitirá la entrada de cualquier letra
while letra != '0':
    letra = input("Ingrese una letra (D, J, M). Ingrese 0 para continuar\n> ")
    if letra != '0':
        resultado = buscarNombre(lista,letra)
        if resultado != []:
            for i in resultado:
                print(i)
        else:
            print(f"No se han encontrado nombres que empiezen con {letra}")




