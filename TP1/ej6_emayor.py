# Una palabra es alfabética si todas sus letras están 
# ordenadas alfabéticamente. Por ejemplo: amor, chino e himno
# son palabras alfabéticas. Diseñar un programa que 
# lea una palabra y nos diga si es alfabética o no.

# Se convierte la palabra en lista y se la ordena. sorted() es "case-sensitive". Las palabras
# que comienzan en mayúscula son menores en orden que las minúsculas (por ASCII)

def esAlfabetica(palabra):
    palabra_lista = list(palabra)
    palabra_ord = sorted(list(palabra))
    if palabra_ord == palabra_lista:
        return True
    return False

palabra = input("Ingrese una palabra\n> ")
if esAlfabetica(palabra):
    print("La palabra es alfabética")
else:
    print("La palabra no es alfabética")