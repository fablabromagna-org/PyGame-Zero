
import pgzrun

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = alien.width + 400
HEIGHT = alien.height + 50

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.left = 0

pgzrun.go()
