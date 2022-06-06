# Escribir una función espejo(q) que acepte una cola de letras como parámetro y que agregue los elementos al final
# de la cola en orden inverso, formando un string “capicúa”:

from tads import Pila, Cola

def espejo(cola):
    resultado = ""
    pilaAux = Pila()
    while not cola.estaVacia():
        lAux = cola.sacar()
        pilaAux.apilar(lAux)
        resultado += lAux
    while not pilaAux.estaVacia():
        resultado += pilaAux.desapilar()
    for i in resultado:
        cola.meter(i)
    return cola

cola = Cola()
cola.meter("a")
cola.meter("b")    
cola.meter("c")    
cola.meter(5)

capicua = espejo(cola)

print(capicua)

    
