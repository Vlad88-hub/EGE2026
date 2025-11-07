from  turtle import *

screensize(3000, 3000)
tracer(0)

m = 30
rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)

up()
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * m, y * m)
        dot(4, 'green')

update()
done()

z = 113