import pygame as pg
import sys

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

pg.init()
ping = pg.mixer.Sound('sonidos/ping.wav')

pantalla = pg.display.set_mode((800, 600))


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

game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            print("Fin")
            game_over = True

    if x > 800-ancho_bola or x < ancho_bola:
        velocidadX = -velocidadX
        ping.play()

    if x1 > 800-ancho_bola or x1 < ancho_bola:
        velocidadX1 = -velocidadX1
        ping.play()
        
    if y > 600-ancho_bola or y < ancho_bola:
        velocidadY = -velocidadY
        ping.play()
        
    if y1 > 600-ancho_bola or y1 < ancho_bola:
        velocidadY1 = -velocidadY1
        ping.play()

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




        