# core/maze.py
# Genera la matriz del laberinto con obstáculos aleatorios

import random

# Devuelve una matriz n x n con obstáculos (1) y espacios libres (0)
def generar_laberinto(n, num_obstaculos):
    matriz = [[0 for _ in range(n)] for _ in range(n)]  # Inicializamos con 0
    posibles = [(x, y) for x in range(n) for y in range(n)]  # Todas las coordenadas posibles
    obstaculos = random.sample(posibles, num_obstaculos)     # Seleccionamos al azar

    # Colocamos obstáculos (1) en la matriz
    for (x, y) in obstaculos:
        matriz[y][x] = 1

    return matriz
