# Escribir un programa que valide los paréntesis de una expresión usando una pila, 
# y devuelva “correcta” en caso de que los paréntesis estén correctamente utilizados, 
# e “incorrecta” para aquellos casos en que haya un error.

from tads import Pila

def verificarParentesis(expresion):
    expresionPila = Pila()
    esCorrecta = True
    i = 0
    while esCorrecta and i < len(expresion):
        # Apilamos los parentesis abiertos
        if expresion[i] == "(":
            expresionPila.apilar(expresion[i])
        # Desapilamos los cerrados
        elif expresion[i] == ")":
            if not expresionPila.estaVacia():
                expresionPila.desapilar()
            else:
                # Si intentamos desapilar y la pila esta vacia significa que sobran parentesis derechos
                esCorrecta = False
        i+=1
    # Si la pila no está vacía y la misma sigue siendo correcta, entonces sobran parentesis izquierdos
    if not expresionPila.estaVacia() and esCorrecta:
        esCorrecta = False
    return esCorrecta

expresion = input("Ingrese una expresion con parentesis\n> ")

if verificarParentesis(expresion):
    print("La expresión es correcta")
else:
    print("La expresión es incorrecta")