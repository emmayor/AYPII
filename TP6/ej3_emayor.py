# Escriba dos métodos NO recursivos que encuentren:
# (a) El mínimo de un ABB
# (b) El máximo de un ABB

from ArbolBB import ArbolBB

arbol = ArbolBB(5,ArbolBB(3, ArbolBB(1), ArbolBB(4)),ArbolBB(7,ArbolBB(6),ArbolBB(10)))

# Los métodos ya fueron agregados a la clase:

# def maximo(self):
#         actual = self
#         while actual.subder() != None:
#             if actual.subder() != None:
#                 actual = actual.subder()
#         return actual.valor()
# def minimo(self):
#     actual = self
#     while actual.subizq() != None:
#         if actual.subizq() != None:
#             actual = actual.subizq()
#     return actual.valor()
        
            
print(arbol.maximo())
print(arbol.minimo())
        
    
        
    