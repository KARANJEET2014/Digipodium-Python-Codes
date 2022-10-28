import pgzrun

HEIGHT = 500
WIDTH = 800

def scale

p = Actor('ironman', (100,100))

def draw():
    screen.fill('blue')
    p.draw()

def update():
    p.x+=1

pgzrun.go()