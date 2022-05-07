# Escriba un método espejo() para extender el TAD Cola, que agregue los elementos al final de la cola en orden
# inverso, formando una cola “capicúa”.
# Resuelva y calcule el orden de complejidad de la función espejo() resultante.

# En el archivo tads.py se encuentra el análisis de complejidad

from tads import ColaExt

cola = ColaExt()
cola.meter("a")
cola.meter("b")    
cola.meter("c")    
cola.meter("d")

cola_espejada = cola.espejo()

print(cola_espejada)

