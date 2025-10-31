from turtle import *

screensize(10000,10000)
tracer(0)
m = 10

for i in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(8 * m)
lt(90)
down()
for i in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)
up()
for x in range(-1, 96):
    for y in range(-105, 1):
        goto(x * m, y * m)
        dot(4, 'green')
update()
done()
z = 17*22

