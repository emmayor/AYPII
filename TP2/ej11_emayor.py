# ¿Puede hacer un dibujo como el anterior… con triángulos? ¿Qué triángulos debería usar?

from turtle import *
from math import sqrt

def inicializar():
    penup()
    hideturtle()
    setx(xcor()-(lado*m)/2)
    sety(ycor()+(lado*n)/2)
    pensize(2)
    showturtle()
    speed(100)
    pendown()

def triangulo(lado, sentido):
    if sentido:
        s = 1
    else:
        s = -1
    forward(lado)
    right(90*s)
    forward(lado)
    right(135*s)
    forward(hipotenusa)
    left(135*s)

def grilla(m,n):
    xpos = xcor()
    for i in range(n):
        setx(xpos)
        for j in range(m):
            fillcolor("#103f79")
            begin_fill()
            triangulo(lado,True)
            end_fill()
            fillcolor("#f3b229")
            begin_fill()
            triangulo(lado,False)
            end_fill()
            forward(lado)
        ypos = ycor()-lado
        sety(ypos)
                
m = 6
n = 6
lado = 50
hipotenusa = sqrt(2*(lado**2))
inicializar()
grilla(m,n)
input()
        


