# Realizar un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes
# de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
# Siempre se debe dar el menor número de billetes posibles (para 100€ entregaría un único billete, no diez de 10€)     

# SOLUCIÓN:
# Usamos división exacta (//) para calcular la cantidad de billetes/monedas con la que nos podemos acercar, comenzando
# por el de 500 y siguiendo en orden "decreciente" hasta el 2. Luego de cada división tomamos el monto original y 
# nos quedamos con el resto de la misma división que hicimos y probamos con otra nominación.
# Si ya no es divisible por 2, entonces quedará usar monedas de 1 para representar la cantidad restante. 

nominaciones = (500, 200, 100, 50, 20, 10, 5, 2, 1)

def ContarBilletes(monto):
    billetes = [0] * 9
    for n in nominaciones[:7]:
        cuenta = monto // n
        if (cuenta) > 0:
            billetes[nominaciones.index(n)]+=cuenta
            monto = monto % n
    billetes[8] = monto
    return billetes                                                           

monto = int(input('Ingrese un monto\n> '))
resultado = ContarBilletes(monto)
for i in range(0,9):
    if resultado[i] > 0:
        print(f"Billetes de €{nominaciones[i]}: {resultado[i]}")

        
    
            


