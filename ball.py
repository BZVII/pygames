import pygame as pg
import sys
from random import randrange

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

pg.init()
ping = pg.mixer.Sound('sonidos/ping.wav')

pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

ancho_bola = 10

x = (800-20)//2
y = (600-20)//2

x1 = ancho_bola
y1 = ancho_bola

bolas = []
for i in range(randrange(5,25)):
    bolas.append({  'x': randrange(ancho_bola, ANCHO_PANTALLA-ancho_bola),
                    'y': randrange(ancho_bola, ALTO_PANTALLA-ancho_bola),
                    'vx': randrange(5, 11), 'vy': randrange(5, 11),
                    'color': (randrange(256), randrange(256), randrange(256))
    })




'''
Funciones genericas control gráfico
'''

def choque_bordes_X(x, w):
    if x > ANCHO_PANTALLA-w or x < w:
        ping.play()
        return -1
    return 1

def choque_bordes_Y(y, h):
    if y > ALTO_PANTALLA-h or y < h:
        ping.play()
        return -1
    return 1


game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            print("Fin")
            game_over = True

    for bola in bolas:
        bola['vx'] *= choque_bordes_X(bola['x'], ancho_bola)
        bola['x'] += bola['vx']
        bola['vy'] *= choque_bordes_Y(bola['y'], ancho_bola)
        bola['y'] += bola['vy']
        print(bola)


    pantalla.fill(AZUL)
    for bola in bolas:
        pg.draw.circle(pantalla, bola['color'], (bola['x'], bola['y']), ancho_bola)

    pg.display.flip()

pg.quit()
sys.exit()




        