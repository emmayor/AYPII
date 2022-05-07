# Diseñar un programa que, dados dos números enteros, muestre por pantalla uno de los siguientes mensajes,
# dependiendo de la verificación de la condición que corresponda.
# El segundo es el cuadrado exacto del primero.
# El segundo es menor que el cuadrado del primero.
# El segundo es mayor que el cuadrado del primero.

# LECTURA DE DATOS
a = int(input('Ingrese un número A\n> '))
b = int(input('Ingrese un número B\n> '))

# VERIFICACION DE DATOS E IMPRESIÓN DEL MENSAJE
if (a*a) == b:
    print("El segundo número es el cuadrado exacto del primero")
else:
    if (a*a) > b:
        print("El segundo es menor que el cuadrado del primero.")
    else:
        print("El segundo es mayor que el cuadrado del primero.")

