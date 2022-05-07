# Ejercicio 4
# Diseñar una función que reciba los tres coeficientes de una ecuación de segundo grado, y devuelva una lista con
# sus soluciones reales.
# Si la ecuación sólo tiene una solución real, devuelve una lista con dos copias de la misma. Si no tiene solución real
# alguna o si tiene infinitas soluciones, devuelve una lista con dos copias del valor None. asdalskdjlaksjdlkajsldkjalskdjalskjdlaksjdlaksjdlkajsldkajsdlkjasldk

from math import sqrt

# Función original usando try/except para manejar el error de meter un número sdasdasd
# negativo en sqrt

# def baskhara(a, b, c):
#     try:
#         delta = sqrt((b*b)-(4*a*c))
#         x1 = (-b+delta)/(2*a)
#         x2 = (-b-delta)/(2*a)
#     except: 
#         x1 = None
#         x2 = None
#     return (x1, x2)

# Función alternativa que usa cosas que ya usamos

def baskhara(a, b, c):
    delta = (b*b)-(4*a*c)
    if delta >= 0:
        delta = sqrt(delta)
        x1 = (-b+delta)/(2*a)
        x2 = (-b-delta)/(2*a)
    else:
        x1 = None
        x2 = None
    return (x1, x2)


a = float(input("Ingrese un número para A \n> "))
b = float(input("Ingrese un número para B \n> ")) 
c = float(input("Ingrese un número para C \n> "))

raices = baskhara(a, b, c)

print(f"Las raíces son {raices}")

