# Escribir un programa que chequee si un string ingresado es un palíndromo o no, usando una pila. Nota: un palíndromo es una palabra
# o expresión que se lee igual de izquierda a derecha que de derecha a izquierda.

from tads import Pila

caracteresBasura = {
'á':'a',
'é':'e',
'í':'i',
'ó':'o',
'ú':'u',
' ':'',
';':'',
'.':'',
'!':'',
}

# No nos interesan ni los acentos, ni los ni los espacios en blanco ni las mayúsculas, 
# lo importante es que se pueda leer en ambos sentidos con una fonetica similar.
# Existen otras letras con acentos, como 'ý', pero consideraremos
# como mucho los que se utilizan en el español, más los signos de puntuación 
def Normalizar(expresion):
    normalizada = expresion.lower()
    for i in caracteresBasura:
        normalizada = normalizada.replace(i, caracteresBasura[i])
    return normalizada

# Luego de normalizar la expresion, la invertimos
def Invertir(expresion):
    expresionPila = Pila()
    expInvertida = ""
    for i in expresion:
        expresionPila.apilar(i)
    while not expresionPila.estaVacia():
        expInvertida += expresionPila.desapilar()
    return expInvertida

expresion = input("Ingrese un palíndromo\n> ")
expNormalizada = Normalizar(expresion)
expInvertida = Invertir(expNormalizada)

# Si la expresión normalizada y su version espeja son iguales entonces
# estamos ante un palíndromo
if expNormalizada == expInvertida:
    print("Es palindromo")
else:
    print("No es palindromo")