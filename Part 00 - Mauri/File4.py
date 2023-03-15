
import pgzrun

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = alien.width + 400
HEIGHT = alien.height + 50

direction=0

def draw():
    screen.clear()
    alien.draw()

def update():
    global direction
    if( direction == 0 ) :
        alien.left += 2
        if alien.left > WIDTH:
            direction = 1
    else:
        alien.left -= 2
        if alien.left <= 0:
            direction = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
        
pgzrun.go()
