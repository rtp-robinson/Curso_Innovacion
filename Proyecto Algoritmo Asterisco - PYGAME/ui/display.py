# ui/display.py
# Se encarga de dibujar el laberinto y sus elementos visuales en pantalla

import pygame

# Dibuja cada celda del laberinto, incluyendo obstáculos, inicio, meta y camino
def dibujar_laberinto(screen, matriz, inicio, meta, n, CELL_SIZE, camino=[], explorados=set()):
    for y in range(n):
        for x in range(n):
            rect = pygame.Rect(x*CELL_SIZE, (n-1-y)*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pos = (x, y)

            # Asignamos colores según el tipo de celda
            if pos == inicio:
                color = (0, 255, 0)           # Verde: inicio
            elif pos == meta:
                color = (255, 0, 0)           # Rojo: meta
            elif pos in camino:
                color = (30, 144, 255)        # Azul: camino
            elif pos in explorados:
                color = (173, 216, 230)       # Celeste: explorados
            elif matriz[y][x] == 1:
                color = (100, 100, 100)       # Gris: obstáculo
            else:
                color = (255, 255, 255)       # Blanco: libre

            pygame.draw.rect(screen, color, rect)          # Pintamos celda
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)    # Dibujamos borde
