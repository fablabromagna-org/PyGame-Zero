# Vedi qui...
# https://pygame-zero.readthedocs.io/en/stable/introduction.html

import pgzrun
import time

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
        if alien.left > WIDTH-alien.width:
            direction = 1
    else:
        alien.left -= 2
        if alien.left <= 0:
            direction = 0
        
pgzrun.go()
