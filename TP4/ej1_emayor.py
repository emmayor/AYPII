# Una letra significa apilar() y un asterisco, desapilar() en la siguiente secuencia. Si se parte de una estructura vacía,
# ¿cómo quedará la pila luego de aplicar dicha secuencia? Y si desapilamos los valores que quedan, cuales son las
# cadenas de caracteres que se forman?
# (a) E * S U N * * A * P I Ñ * * * A , * P A * T * O
# (b) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * *

# Quedan formadas las palabras "SAPO" y "COVID"

from tads import Pila

cadena1 = "E*SUN**A*PIÑ***A,*PA*T*O"
cadena2 = "CAY**OPO**RL*A**VENT***IL*AC*IO***N*DELBAÑO******"

def transformarPila(pila, cadena):
    for i in cadena:
        if i == '*':
            pila.desapilar()
        else:
            pila.apilar(i)
    return pila

pila1 = Pila()
pila2 = Pila()
transformarPila(pila1,cadena1)
transformarPila(pila2,cadena2)

print(pila1)
print(pila2)
