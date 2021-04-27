import pygame as pg
import sys

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
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

color = ROJO
color1 = (0, 255, 0)
velocidadX = 5
velocidadY = 5
velocidadX1 = 7
velocidadY1 = -5

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

    velocidadX *= choque_bordes_X(x, ancho_bola)
    velocidadY *= choque_bordes_Y(y, ancho_bola)
    velocidadX1 *= choque_bordes_X(x1, ancho_bola)
    velocidadY1 *= choque_bordes_Y(y1, ancho_bola)

    y += velocidadY
    x += velocidadX
    y1 += velocidadY1
    x1 += velocidadX1

    pantalla.fill(AZUL)
    pg.draw.circle(pantalla, color, (x, y), ancho_bola)
    pg.draw.circle(pantalla, color1, (x1, y1), ancho_bola)
    pg.display.flip()

pg.quit()
sys.exit()




        