"""
Este código está completo,
ele desenha vários círculos
usando o módulo turtle.
"""

import turtle


def desenhaCirculo(): # Cria circulos
    alex.speed(10)
    alex.circle(25, 360)
    alex.left(30)
    alex.left(45)
    alex.left(90)
    alex.left(180)


tela = turtle.Screen()

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")

for i in range(24):
    desenhaCirculo()

alex.penup()
alex.color("red")
alex.goto(100, 100)
alex.pendown()
for i in range(24):
    desenhaCirculo()

alex.penup()
alex.color("blue")
alex.goto(-100,-100)
alex.pendown()
for i in range(24):
    desenhaCirculo()

alex.penup()
alex.color("Aqua")
alex.goto(-180,0.00)
alex.pendown()
for i in range(24):
    desenhaCirculo()

alex.penup()
alex.color("DarkViolet")
alex.goto(200,0.00)
alex.pendown()
for i in range(24):
    desenhaCirculo()

tela.exitonclick()
