from turtle import*
i=1

speed('slowest')
while True:
    fd(10+i)
    left(360/5)
    i=i+5
    write(i)
    if i>500:
        break

mainloop()