# Ejercicio 9
# Escriba un algoritmo para calcular los números combinatorios en forma recursiva, sabiendo que:
# (n,m) = (n-1,m)+(n-1,m-1)
# (n,n) = (n,0) = 1

def combinatorios(n,m):
    if (m == 0) | (m == n):
        return 1
    else:
        return combinatorios(n-1,m)+combinatorios(n-1,m-1)

print(combinatorios(1,6))

