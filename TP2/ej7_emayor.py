# a. Escribir un programa que calcule el máximo común divisor (mcd) de dos números n y m, utilizando el algoritmo
# de Euclides, un método que se conoce desde la antigüedad y que se suele considerar el primer algoritmo
# propuesto por el hombre. El algoritmo dice así:
# Calcula el resto de dividir el mayor de los dos números por el menor de ellos. Si el resto es cero,
# entonces el máximo común divisor es el menor de ambos números. Si el resto es distinto de cero, el
# máximo común divisor de n y m es el máximo común divisor de otro par de números: el formado por
# el menor de n y m y por dicho resto. (Para calcular el resto, se puede utilizar el operador %)
# b. Hacer una traza de las llamadas a mcd para los números 1470 y 693.

def mcd(n,m):
    numeros = sorted([m,n])
    resto = numeros[1] % numeros[0]
    if resto == 0:
        return numeros[0]
    else:
        return mcd(resto,numeros[0])

m = int(input("Ingrese un número m:\n> "))
n = int(input("Ingrese un número n:\n> "))
res = mcd(m,n)
print(f"El MCD entre {m} y {n} es {res}.")
    
