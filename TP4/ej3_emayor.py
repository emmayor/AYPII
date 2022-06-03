# Escribir un programa que lea una secuencia de caracteres y los imprima en orden inverso, usando el TAD Pila. La
# secuencia termina al ingresar un * (asterisco).
# Analizar la eficiencia del algoritmo resultante, buscando la función que representa el código y la cota superior (peor
# caso).

# El orden de complejidad del algoritmo es de Θ(n), ya que por cada caracter se debe imprimir y verificar que la lista este vacía 

from tads import Pila

cr = ''
cadena = Pila()

while cr != '*':
    cr = input('Ingrese un caracter. * para terminar \n> ')
    cadena.apilar(cr)

# En vez de chequear si lo que se ingreso fue un asterisco, lo sacamos, porque sabemos que 
# está al final de la pila. Cuesta menos :)
cadena.desapilar()

while not cadena.estaVacia():
    print(cadena.desapilar(), end='')



