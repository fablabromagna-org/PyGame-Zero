
# preso da qui
# https://new.pythonforengineers.com/blog/your-first-game-in-python-in-less-than-30-minutes/

#
# sistemato e commentato da maurizio.conti@fablabromagna.org
# 15 marzo 2023
#
import pgzrun
import random

TITLE = "FabLab-rkanoid"
WIDTH = 800
HEIGHT = 500

# Actor è l'oggetto che gestisce le immagini
paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 100
ball.y = 300

ball_x_speed = -4
ball_y_speed = -4

# le parentesi quadre indicano in python una lista mutabile
# le parentesi tonde () sono collezioni immutabili
# le parentesi graffe {} sono i dizionari (coppie nome=valore)

# Qui usiamo una lista per tenere i matttoncini
# (all'inizio è vuota)
bars_list = []

# Con questo metodo riempiamo
# una riga da 8 mattoncini dello stesso colore
def place_bars( x, y, image ):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)

# posizione iniziale del blocco di mattoncini
x = 120
y = 100

# questa lista contiene i nomi delle immagini dei mattoncini
coloured_box_list = ["element_blue_rectangle_glossy.png", "element_green_rectangle_glossy.png","element_red_rectangle_glossy.png"]

# si passa tutti i nomi delle immagini e crea una striscia da 8 per ogni tipo
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50


# draw viene chiamato dal sistema quando qualcosa cambia
# utile per cose che non sempre cambiano, come lo sfondo
def draw():
    
    # la funziona blit, disegna una immagine alla posizione indicata
    screen.blit("background.png", (0,0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()


# update invece viene comunque chiamato
# (60 volte al secondo)
def update():
    
    # con global accediamo alla variabile che
    # abbiamo definito all'inizio...
    global ball_x_speed, ball_y_speed
    
    # keyboard gestisce la tastiera
    if keyboard.left:
        paddle.x = paddle.x - 5
        
    if keyboard.right:
        paddle.x = paddle.x + 5

    # aggiorniamo la posizione della pallina
    update_ball()
    
    # se la pallina collide con un mattone
    # lo togliamo dalla lista e cambiamo direzione verticale (y)
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1

    # se la pallina collide con il paddle
    if paddle.colliderect(ball):

        # cambiamo di sicuro la direzione verticale (y)
        ball_y_speed *= -1

        # ... ma a caso cambiamo anche la direzione orizzontale (x)
        rand = random.randint(0,1)
        if rand:
            ball_x_speed *= -1

def update_ball():
    global ball_x_speed, ball_y_speed

    # muove la pallina in entrambe le direzioni x e y
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    
    # se tocca i bordi laterali, inverte la direzione x
    if (ball.x >= WIDTH) or (ball.x <=0):
        ball_x_speed *= -1

    # se tocca i bordi superiori, inverte la direzione y
    if (ball.y >= HEIGHT) or (ball.y <=0):
        ball_y_speed *= -1

pgzrun.go()