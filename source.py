# coding=utf-8

# importa la librería Pygame
from pygame.constants import K_SPACE, KEYDOWN, KEYUP, K_RIGHT, K_UP,\
    K_LEFT, K_DOWN
import pygame
FLECHAS = (K_RIGHT, K_UP, K_LEFT, K_DOWN)
DIRECCIONES = ('derecha', 'arriba', 'izquierda', 'abajo')


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption(u'Estado de teclas')

    # establece el tamaño de la ventana
    pygame.display.set_mode((400, 400))

    # crea un reloj
    clock = pygame.time.Clock()

    # ¿la aplicación está ejecutándose?
    is_running = True
    space = False
    # si la aplicación está ejecutándose
    while is_running:
        # limita las actualizaciones a 5 cuadros por segundo (FPS)
        clock.tick(5)

        # obtiene los eventos de la cola de eventos
        for event in pygame.event.get():
            # si se presiona el botón 'cerrar' de la ventana
            if event.type == pygame.QUIT:
                # detiene la aplicación
                is_running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
                if space and event.key in FLECHAS:
                    direcc = FLECHAS.index(event.key)
                    print('ataque ' + DIRECCIONES[direcc])
            elif event.type == KEYUP and event.key == K_SPACE:
                space = False

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
