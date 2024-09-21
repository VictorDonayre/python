from turtle import *
import colorsys
import math 

# Configuración inicial
speed(0)
bgcolor('black')


# Generando los pétalos
goto(0, -40)

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125, 1, 1)
        color(c)
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Generando la parte central de la flor 
color('black')
shape('turtle')
fillcolor('brown')
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta) 
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

# Agregar texto nuevamente en la parte superior
penup()
goto(0, 240)
color('white')
write('For you ♡', align='center', font=('Comic Sans MS', 24, 'bold'))

hideturtle()
done()