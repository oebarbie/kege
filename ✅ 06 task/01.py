from turtle import *

screensize(10_000, 10_000)
tracer(0)
lt(90)
pd()
rt(45)
k = 10
for _ in range(25):
    fd(55)
    rt(90)

for x in range(-55, 90):
    for y in range(-55, 55):
        goto(x*k, y*k)
        dot(3)

update()