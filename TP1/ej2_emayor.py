# Escribir un programa que permita evaluar el polinomio x^4 + x^3 + 2x^2 − x. 
# Luego, escribir otro programa que solicite valores de x por teclado y calcule
# el valor del polinomio para ellos, mostrando el resultado. Es importante 
# tener en cuenta cuál es la modularización adecuada del problema y cuál sería 
# el criterio de parada al ingreso de datos.

# Devolver resultado de x^4 + x^3 + 2x^2 − x
def EvaluarPolinomio(x):
    return x**4 + x**3 + 2*(x*x) - x

def LeerDatos():
    valor = float(input('> '))
    return valor

print("Ingrese un valor para X")
x = LeerDatos()
resultado = EvaluarPolinomio(x)
print(f"({x} ^ 4) + ({x} ^ 3) + (2 * {x} ^ 2) - {x} = {resultado}")

