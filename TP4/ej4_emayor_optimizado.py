# Escribir un programa que chequee si un string ingresado es un palíndromo o no, usando una pila. Nota: un palíndromo es una palabra
# o expresión que se lee igual de izquierda a derecha que de derecha a izquierda.

# OPTIMIZACIONES RESPECTO DE LA VERSION ANTERIOR:
# En lugar de invertir la cadena completa y compararla con la original, 
# se implementó un nuevo algoritmo "esPalindromo" que recorra la cadena completa COMO MAXIMO
# UNA SOLA VEZ (cuando la misma es un palindromo). Sólo se apila la primera
# mitad de la misma y se desapila mientras se compara con la segunda mitad de 
# la cadena original. Esto reduce el tiempo de ejecución aproximadamente a la mitad
# de lo que tardaba el anterior. (antes: Θ(2n), ahora: O(n), Ω(n/2))
# En la carpeta "palindromos_perf" se encuentran ambas versiones preparadas para
# medir el tiempo de normalizacion y comparacion, junto a un archivo con 
# mas de 400000 caracteres iguales (que es un palindromo)

from tads import Pila

# No nos interesan ni los acentos, ni los ni los espacios en blanco ni las mayúsculas, 
# lo importante es que se pueda leer en ambos sentidos con una fonetica similar.
# Existen otras letras con acentos, como 'ý', pero consideraremos 
# algunos de los que se utilizan en el español, más los signos de puntuación

caracteresBasura = {
'á':'a',
'é':'e',
'í':'i',
'ó':'o',
'ú':'u',
' ':'',
';':'',
'.':'',
',':'',
'!':'',
}

# Normalizar la expresión implica:
# + Pasarla a minúsculas
# + Quitar los caracteres basura 
# + Si la cantidad de caracteres es impar, quitar el del medio

def Normalizar(expresion):
    normalizada = expresion.lower() 
    for i in caracteresBasura: 
        normalizada = normalizada.replace(i, caracteresBasura[i])
    if len(normalizada) % 2: 
        listaNormalizada = list(normalizada) 
        listaNormalizada.pop(len(normalizada)//2) 
        normalizada = ''.join(listaNormalizada)
    return normalizada

# Luego de normalizar la expresion, verificamos si es un palíndromo. Para eso, apilamos
# sólo la mitad de la expresión -por eso quitamos el caracter del medio si la longitud de la expresion es impar-
# y comparamos con la segunda mitad de la expresion a medida que desapilamos
# Si no dan distinto en ningun momento, estamos ante un palíndromo

def esPalindromo(expresion):
    long = len(expresion)//2
    mitad = Pila()
    # PRIMERA MITAD: Se apila
    for i in range(long):
        mitad.apilar(expresion[i])
    i = long 
    # SEGUNDA MITAD: Se compara la mitad apilada con la segunda mitad sin apilar
    while not mitad.estaVacia():
        if mitad.desapilar() != expresion[i]:
            return False
        i+=1
    return True

expresion = input("Ingrese un palíndromo\n> ")
expNormalizada = Normalizar(expresion)

if esPalindromo(expNormalizada):
    print("Es palindromo")
else:
    print("No es palindromo")

