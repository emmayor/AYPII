# En la siguiente secuencia, una letra significa encolar() y un asterisco, desencolar(). Mostrar la secuencia de
# valores que devuelve el método desencolar() para todos los elementos restantes de la cola, una vez que se aplicó
# la secuencia de operaciones a una cola vacía.
# (a) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * * D E L B A Ñ O * * * * * *
# (b) P A * S O P * * O * R T * U C * * A S * A *

# Quedan formadas las palabras "BAÑO" y "CASA"

from tads import Cola

cadena1 = "CAY**OPO**RL*A**VENT***IL*AC*IO***N**DELBAÑO******"
cadena2 = "PA*SOP**O*RT*UC**AS*A*"

def transformarCola(cola, cadena):
    for i in cadena:
        if i == '*':
            cola.sacar()
        else:
            cola.meter(i)
    return cola

cola1 = Cola()
cola2 = Cola()
transformarCola(cola1,cadena1)
transformarCola(cola2,cadena2)

print(cola1)
print(cola2)