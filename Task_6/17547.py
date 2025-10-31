from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()
for x in range(-80, 8):
    for y in range(-12, 72):
        goto(x * m, y * m)
        dot(4, 'green')
update()
done()
z = 84*78+8*13-7*4
