from turtle import *


tracer(False)
k = 25
pendown()
for i in range(2):
    forward(9 * k)
    right(90)
    forward(15 * k)
    right(90)
penup()
forward(12 * k)
right(90)
pendown()
for i in range(2):
    forward(6 * k)
    right(90)
    forward(12 * k)
    right(90)
penup()
for x in range(0, 30):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(5)

exitonclick()