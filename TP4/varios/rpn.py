from tads import Pila

def calculadoraPolaca(elementos):
    """ Dada una lista de elementos que representan las componentes de una 
    expresión en notación polaca inversa, evalúa dicha exporesión."""
    p = Pila()
    for elemento in elementos:
        if elemento not in ('+','-','*','/'):
            # Es un número, lo convierte
            numero = float(elemento)
            p.apilar(numero)
        else:
            # Es un operador
            a2 = p.desapilar()
            a1 = p.desapilar()
            resultado = eval("a1"+elemento+"a2")
            p.apilar(resultado)
        # Al terminar el resultado es el último elemento agregado a la píla
    resultado = p.desapilar()
    return resultado

expresion = input("Ingrese la expresión a evaluar\n> ")
elementos = expresion.split()
print(elementos)
print(calculadoraPolaca(elementos))
