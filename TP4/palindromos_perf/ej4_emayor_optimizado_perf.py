# Escribir un programa que chequee si un string ingresado es un palíndromo o no, usando una pila. Nota: un palíndromo es una palabra
# o expresión que se lee igual de izquierda a derecha que de derecha a izquierda.

from tads import Pila
from time import perf_counter_ns

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

def Normalizar(expresion):
    normalizada = expresion.lower() # Pasamos a minuscula
    for i in caracteresBasura: # Quitamos los caracteres basura
        normalizada = normalizada.replace(i, caracteresBasura[i])
    if len(normalizada) % 2: # Si la longitud de la cadena es impar
        listaNormalizada = list(normalizada) 
        listaNormalizada.pop(len(normalizada)//2) # Quitamos el caracter del medio. Nos servira mas adelante
        normalizada = ''.join(listaNormalizada)
    return normalizada

# Luego de normalizar la expresion, verificamos si es un palíndromo. Para eso, apilamos
# sólo la mitad de la expresión -por eso quitamos el caracter del medio si la longitud de la expresion es impar-
# y comparamos con la segunda mitad de la expresion a medida que desapilamos
# Si no dan distinto en ningun momento, estamos ante un palíndromo

def esPalindromo(expresion):
    long = len(expresion)//2
    mitad = Pila()
    for i in range(long):
        mitad.apilar(expresion[i])
    i = long
    while not mitad.estaVacia():
        if mitad.desapilar() != expresion[i]:
            return False
        i+=1
    return True

file = open("ejemplo.txt",'r')
expresion = file.read()

start = perf_counter_ns()

expNormalizada = Normalizar(expresion)
if esPalindromo(expNormalizada):
    print("Es palindromo")
else:
    print("No es palindromo")
    
time = perf_counter_ns() - start 
print(f'Tiempo: {time*1e-9}')

