from turtle import *

screensize(3000, 3000)
tracer(0)

m = 15
for i in range(2):
    fd(14 * m)
    lt(270)
    rt(180)
    fd(12 * m)
    lt(180)
    rt(90)
up()
fd(9 * m)
rt(90)
rt(180)
fd(7 * m)
rt(180)
lt(90)
down()
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-15, 25):
    for y in range(-15, 15):
        goto(x * m, y * m)
        dot(4, 'green')

update()
done()