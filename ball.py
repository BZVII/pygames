import pygame as pg
import sys

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

pg.init()
ping = pg.mixer.Sound('sonidos/ping.wav')



class Game(object):
    
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))


    def bucle_principal(self):
        ancho_bola = 20
        x = (800-20)//2
        y = (600-20)//2
        color = ROJO
        velocidadX = 5
        velocidadY = 5
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    print("Fin")
                    game_over = True

            if x > 800-ancho_bola or x < ancho_bola:
                velocidadX = -velocidadX
                ping.play()
            if y > 600-ancho_bola or y < ancho_bola:
                velocidadY = -velocidadY
                ping.play()
            y += velocidadY
            x += velocidadX

            self.pantalla.fill(AZUL)
            pg.draw.circle(self.pantalla, color, (x, y), ancho_bola)
            pg.display.flip()

        pg.quit()
        sys.exit()




        