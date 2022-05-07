# Hacer un damero de n x m cuadrados, cada uno de ellos de lado
# x. Tenga en mente modularizar y utilizar las mejores técnicas
# vistas hasta ahora.

from turtle import *

def inicializar():
    penup()
    hideturtle()
    setx(xcor()-(lado*m)/2)
    sety(ycor()+(lado*n)/2)
    pensize(2)
    showturtle()
    speed(100)
    
    pendown()

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)
    forward(lado)

def grilla(m,n):
    xpos = xcor()
    for i in range(n):
        setx(xpos)
        for j in range(m):
            if (j+(i%2))%2 == 0:
                fillcolor("#103f79")
                begin_fill()
                cuadrado(lado)
                end_fill()
            else:
                fillcolor("#f3b229")
                begin_fill()
                cuadrado(lado)
                end_fill()
        ypos = ycor()-lado
        sety(ypos)
            
            
m = 9
n = 13
lado = 50
inicializar()
grilla(m,n)
input()
        


