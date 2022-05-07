# Definir una función recursiva, cuenta_atras(n), que recibe un número natural y cuenta hacia atrás desde ese
# número hasta cero. Cuando llega al final de la cuenta, en vez de imprimir el 0, muestra la palabra “Despegando!”. 

def despegando(n):
    if n == 0:
        print("Despegando!")
    else:
        print(n)
        return despegando(n-1)

n = int(input("Ingrese un número n\n> "))
despegando(n)