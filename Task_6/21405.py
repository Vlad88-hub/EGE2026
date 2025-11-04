from turtle import  *

screensize(3000, 3000)
tracer(0)

m = 15
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(4, 'green')

update()
done()

z = 30
