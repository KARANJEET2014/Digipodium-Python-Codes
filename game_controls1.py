import pgzrun

HEIGHT = 500
WIDTH = 800


p = Actor('ironman', (100,100))

def draw():
    screen.fill('blue')
    p.draw()

def update():
    if keyboard.left:
        p.x -=5
        p.angle = 10
    elif keyboard.right:
        p.x +=5
        p.angle =-10
    elif keyboard.up:
        p.y -=5
    elif keyboard.down:
        p.y +=5
    elif keyboard.SPACE:
        p.angle =180
    else:
        p.angle = 0

pgzrun.go()