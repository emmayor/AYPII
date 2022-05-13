""" AyP II - 2020 - Verónica Botto """
""" Imprime un árbol binario en forma recursiva, segun el algoritmo preorden visto en clase"""
""" Usa la tortuga para dibujar los nodos del arbol, incluyendo lineas conectoras"""

from turtle import *
from ArbolBB import *

def ImprimirABT(arbol):

    """ Pensar como una matriz: se usa la base, #nodos máximo"""
    """ Después se ajusta con las coordenadas y pixeles"""
    tam = 2**(alturaA(arbol)+1) - 1
    pixs = 10                      # Multiplicador x resolución monitor
    if (tam >= 32):
        pixs = 50

    letra=('Arial', 10, 'normal')
    coox = -pixs * (1 + tam//2)     # Ajustar x para centrar en la pantalla
    cooy = 0
    radc = 15

    screensize(pixs*(tam+2))

    exa = 1                         # C/ nodo va a mitad del intervalo exa, exb
    exb = tam

    """ Módulo recursivo: usa el nodo, la profundidad (y) y el intervalo (x)"""  
    ImprimirABT_R(arbol, 0, exa, exb,(pixs, coox, cooy, radc, letra))


def ImprimirABT_R(arbol, prof, exa, exb, t_cfg):
    
    """ Calcular la columna en la que va el nodo """    
    posv = int((exa + exb)/2)
    
    dato = arbol.valor()
    posx = t_cfg[1] + posv * t_cfg[0]
    posy = t_cfg[2] - prof * 5 * t_cfg[0] # ACA SE CAMBIA PARA RESOLUCION
    
    escribir(dato, posx, posy, t_cfg) 

    """ Se dibujan los subarboles, con el intervalo que les corresponde""" 
    if arbol.subizq() is not None:
        # hacer linea de padre a hijo izquierdo
        linea(posx, posy, prof+1, exa, posv-1, t_cfg)
        ImprimirABT_R(arbol.subizq(), prof + 1, exa, posv-1, t_cfg)
        # Reubicar la tortuga en el nodo padre!
        penup()
        hideturtle()
        goto(posx, posy)
        pendown()
        showturtle()
        
    if arbol.subder() is not None:
        # hacer linea de padre a hijo derecho
        linea(posx, posy, prof+1, posv+1, exb, t_cfg)
        ImprimirABT_R(arbol.subder(), prof + 1, posv+1, exb, t_cfg)

def linea(posx, posy, prof, exa, exb, t_cfg):
    
    """ Calcular el nuevo punto, centro del nodo hijo """
    posv = int((exa + exb)/2)
    nposx = t_cfg[1] + posv * t_cfg[0] 
    nposy = t_cfg[2] - prof * 5 * t_cfg[0] # ACA SE CAMBIA PARA RESOLUCION

    """ Guardar orientación de la tortuga, calcular nuevo angulo y distancia"""
    actua = heading()
    hacia = towards(nposx, nposy)
    dista = distance(nposx, nposy)
    
    """ Girar la tortuga y hacer la linea (saltear longitud del radio!)"""
    left(hacia)
    penup()
    forward(int(t_cfg[3]*2/3))  # saltea la longitud del radio (un poco más)
    pendown() 
    forward(dista-2*t_cfg[3])   # hacer la linea más corta, no tocar el círculo
    setheading(actua)     

def escribir(dato, posx, posy, t_cfg):
    """ Escribe el valor del nodo y dibuja el círculo"""
    penup()                     # Ubicar el centro del círculo
    goto(posx, posy-t_cfg[3]/2)
    pendown()
    circle(t_cfg[3])            # Dibujar el círculo
    heading()
    penup()                     
    goto(posx, posy)            # Ubicar el centro, para escribir el dato
    pendown()
    write(dato, align='center', font=t_cfg[4])

""" ******************* Prueba ******************* """
# Cargar un árbol
# test1 = ArbolBB(20)
# lnodos = [10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]
# lnodos = [10, 30, 5, 15, 25, 35]
# lnodos = [10, 30]
# lnodos = [25, 30, 40]

# test1 = ArbolBB('B')
# lnodos = ['A', 'D', 'C', 'H']

# for nod in lnodos:
#   test1.insertar(nod)
# ImprimirABT(test1)
