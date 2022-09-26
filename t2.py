from turtle import *

speed('slowest')

side=5
for i in range(side):
    pencolor('red')
    pensize(1)
    fd(100)
    lt(360/side)
    dot(side*3)
    pensize(4)
    pencolor('green')
    circle(side*10)
mainloop()