# Considere el problema de la multiplicación de matrices. Para dos matrices, con dimensiones A (x, y) y B (y, z)
# donde el producto da como resultado una matriz C donde C [i,j] es el producto de la i-ésima fila de A por la j-ésima
# columna de B.
# Diseñe un algoritmo, analícelo y determine su complejidad de tiempo usando notación asintótica. Luego
# codifíquelo en Python, usando listas para las matrices, y determine la cantidad de operaciones para la
# multiplicación de matrices cuadradas (A y B de nxn), en los casos en que n vale 10, 20 y 50. Puede utilizar lineas
# adicionales en el programa para obtener estos valores.

# Se estima f(n) = 8n^2 + 3n + 5, o sea, O(n^2)
#
# CANTIDAD DE INSTRUCCIONES:
#
# Para n = 10: 8000000000313 instrucciones
# Para n = 20: 335544320000000000000000001213 instrucciones
# Para n = 50: 177635683940025046467781066894531250000000000000000000000000000000000000000000000000007513 instrucciones

from random import randint

def genMatriz(n):
    matriz = [0] * n
    for i in range(n):
        matriz[i] = [0] * n
        for j in range(n):
            matriz[i][j] = randint(0,10)
    return matriz

def multMatriz(a, b):
    n = len(a[0])                   # 3: Asignación, acceso a lista y cálculo de longitud
    mat_c = [0] * n                 # 2: Asignación y multiplicación
    cuenta = 5
    for i in range(n):
        mat_c[i] = [0] * n
    for c in range(n):              # 1
        cuenta+=1
        for i in range(n):          # 1
            suma = 0                # 1
            for j in range(n):      # 1
                suma += mat_a[i][j]*mat_b[j][c] # 6
                cuenta += 7*n**3   
            mat_c[i][c] = suma
            cuenta += 3*n*n
    cuenta += 1                     # 1: Return
    return [mat_c, cuenta]

n = int(input("Ingrese el tamaño de la matriz\n> "))

mat_a = genMatriz(n)
mat_b = genMatriz(n)
mat_c = multMatriz(mat_a, mat_b)
print(f"Se ejecutaron {mat_c[1]} instrucciones")





