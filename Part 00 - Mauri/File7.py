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

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    # una specie di sleep ma non bloccante...
    clock.schedule_unique(set_alien_normal, 1.0)
    
def set_alien_normal():
    alien.image = 'alien'

        
pgzrun.go()
