# main.py
# Archivo principal que coordina la interfaz gráfica y el algoritmo A*

import pygame
import sys
import time

# Importamos funciones de nuestros módulos personalizados
from ui.dialogs import pedir_parametros           # Ventana emergente para ingresar tamaño y obstáculos
from ui.dialogs import mostrar_mensaje
from core.maze import generar_laberinto           # Función que genera una matriz con obstáculos
from ui.display import dibujar_laberinto          # Función que dibuja la matriz en pantalla
from algorithms.astar import a_estrella           # Implementación del algoritmo A*

# Pedimos al usuario el tamaño del laberinto y la cantidad de obstáculos
n, num_obstaculos = pedir_parametros()
CELL_SIZE = 50                                     # Tamaño de cada celda en píxeles
WIDTH = HEIGHT = n * CELL_SIZE                     # Dimensiones de la ventana gráfica

# Inicializamos la interfaz de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creamos la ventana con las dimensiones calculadas
pygame.display.set_caption("A* Laberinto Simple Modular")
clock = pygame.time.Clock()                        # Usamos un reloj para limitar los FPS

# Creamos la matriz de obstáculos
matriz = generar_laberinto(n, num_obstaculos)

inicio = None      # Coordenadas del punto de inicio
meta = None        # Coordenadas del punto objetivo
camino = []        # Lista que almacenará el camino más corto encontrado

# Función que permite visualizar los nodos que el algoritmo va explorando
def mostrar_explorados(explorados):
    dibujar_laberinto(screen, matriz, inicio, meta, n, CELL_SIZE, explorados=explorados)
    pygame.display.flip()
    pygame.time.delay(20)

# Bucle principal del programa (maneja eventos de usuario)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Salimos del programa

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reiniciar laberinto completamente
                n, num_obstaculos = pedir_parametros()
                WIDTH = HEIGHT = n * CELL_SIZE
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                matriz = generar_laberinto(n, num_obstaculos)
                inicio = None
                meta = None
                camino = []

            elif event.key == pygame.K_a:
                # Permite volver a seleccionar inicio y meta
                inicio = None
                meta = None
                camino = []

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Capturamos clic izquierdo del mouse
            mx, my = pygame.mouse.get_pos()
            x = mx // CELL_SIZE
            y = n - 1 - (my // CELL_SIZE)
            if 0 <= x < n and 0 <= y < n and matriz[y][x] == 0:
                if inicio is None:
                    inicio = (x, y)
                elif meta is None and (x, y) != inicio:
                    meta = (x, y)
                    # Ejecutamos el algoritmo A*
                    camino = a_estrella(matriz, inicio, meta, n, visual_callback=mostrar_explorados)
                    
                    # Si no se encontró camino, mostrar mensaje y permitir seleccionar de nuevo
                    if not camino:
                        mostrar_mensaje("¡No hay ruta posible hacia la meta!")
                        inicio = None
                        meta = None

    
    # Dibujamos la pantalla en cada iteración
    if camino:
        dibujar_laberinto(screen, matriz, inicio, meta, n, CELL_SIZE, camino=camino)
    else:
        dibujar_laberinto(screen, matriz, inicio, meta, n, CELL_SIZE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
