from tads import PilaExt

I, D = 'Izquierdo', 'Derecho'
precedenciaOperadores = {
 '^': (4, D),
 '*': (3, I),
 '/': (3, I),
 '+': (2, I),
 '-': (2, I)}

def hay_que_desapilar(prop1, op2):
    """(there is an operator at the top of the operator stack with greater precedence)
        or (the operator at the top of the operator stack has equal precedence and is left associative))
        and (the operator at the top of the operator stack is not a left parenthesis)"""
    if op2 != "(":
        prop2 = precedenciaOperadores[op2]
        return ((prop1[0] < prop2[0]) or (prop1[0] == prop2[0] and prop2[1] == I))
    return False

def es_operador(untk):
    return (untk in precedenciaOperadores)

""" Algoritmo Shunting Yard """
def shunting_yard(infija):
    salida = []
    pila_de_operadores = PilaExt()
    lista_tokens = infija.split()
    for token in lista_tokens:
        if token.isdigit():
            salida.append(token)
        elif es_operador(token):
            # Procesar operador
            precedenciaOp1 = precedenciaOperadores[token]
            while not pila_de_operadores.estaVacia() and hay_que_desapilar(precedenciaOp1, pila_de_operadores.tope()):
                salida.append(pila_de_operadores.desapilar())
            pila_de_operadores.apilar(token)                
        elif token == "(":
            pila_de_operadores.apilar(token)
        elif token == ")":
            # Procesar el cierre
            while not pila_de_operadores.estaVacia() and (pila_de_operadores.tope()!= "("):
                salida.append(pila_de_operadores.desapilar())
            if not pila_de_operadores.estaVacia() and pila_de_operadores.tope()== "(":
                pila_de_operadores.desapilar()
            else:
                raise ValueError("Expresión mal formada")      
        else:
            raise ValueError("El valor "+token+" no es válido")

    while not pila_de_operadores.estaVacia():
        if pila_de_operadores.tope() in "()":
            raise ValueError("Expresión mal formada")
        else:
            salida.append(pila_de_operadores.desapilar())
    return " ".join(salida)

def main():
    expresion = input("Ingrese la expresión a convertir: ")
    converted = shunting_yard(expresion)
    print(converted)
    print(2)
main()
