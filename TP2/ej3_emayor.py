# A partir del ejercicio anterior, diseñar una función recursiva que, dados m y n, calcule:
# Sumatoria(m,n,i)

def sumatoriaRec2(m,n):
    if n == m:
        return m
    else:
        return n+sumatoriaRec2(m,n-1)

a = sumatoriaRec2(3,9)
print(a)