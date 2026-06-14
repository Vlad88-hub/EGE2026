from turtle import *

screensize(3000, 3000)
tracer(0)
m = 15

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(-20, 24):
    for y in range(-20, 20):
        dot(4, 'green')
        goto(x * m, y * m)

update()
done()