# Se les solicita escribir una función max(s) que acepta una pila de enteros 
# s y devuelve su mayor elemento, es decir
# el entero mayor en la pila. ¿Qué hay que tener en cuenta para resolver este ejercicio?

# Para poder resolver el ejercicio es necesario vaciar la pila para verificar cual de los
# valores es el más grande. 



from tads import Pila

def mayor(pila):
    maximo = 0 # 1
    while not pila.estaVacia(): # 3
        temp = pila.desapilar() # 2
        if temp > maximo:       # 1
            maximo = temp       # 1
    return maximo               # 3+2+1+1+1 = 8
    # Complejidad: 8n

# El orden de complejidad es O(n), y es de orden exacto porque tanto en el mejor como en el peor caso deben hacerse
# n operaciones (Siempre va a ser necesario vaciar la pila para buscar el entero más grande)

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

resultado = mayor(pila)

print(resultado)
print(pila)
