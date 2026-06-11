from turtle import  *

screensize(3000, 3000)
tracer(0)
m =15

for i in range(3):
    fd(27*m)
    rt(90)
    fd(12*m)
    rt(90)

up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77*m)
    rt(90)

up()
for x in range(-20, 28):
    for y in range(-24, 20):
        dot(4, 'green')
        goto(x *m , y*m)

update()
done()