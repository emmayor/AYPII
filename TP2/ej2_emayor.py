# Se puede formular recursivamente la suma de los n primeros números naturales. Diseñar una función recursiva en
# Python que calcule la sumatoria de los n primeros números naturales, según la fórmula:
# Sumatoria(i,1,n) = 1 si n = 1 / n + sumatoria(i,1,n-1) si n > 1

def sumatoriaRec(n):
    if n == 1:
        return 1
    else:
        return n+sumatoriaRec(n-1)

a = sumatoriaRec(3)
print(a)