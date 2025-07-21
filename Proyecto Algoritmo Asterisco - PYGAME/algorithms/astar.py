import math


# Función heurística: distancia euclidiana entre dos puntos (x1,y1) y (x2,y2)
def heuristica(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Algoritmo A*
def a_estrella(matriz, inicio, meta, n, visual_callback=None):
    open_list = [inicio]    # Lista de nodos por explorar
    closed_list = set()     # Conjunto de nodos ya explorados
    padres = {}             # Diccionario para reconstruir el camino
    g = {inicio: 0}         # Coste real desde el inicio hasta cada nodo
    f = {inicio: heuristica(inicio, meta)}  # Coste total estimado f(n) = g(n) + h(n)

    while open_list:
        # Seleccionamos el nodo con menor f(n)
        actual = min(open_list, key=lambda x: f.get(x, float('inf')))
        open_list.remove(actual)
        closed_list.add(actual)

        # Si pasamos una función visual, la llamamos para mostrar exploración
        if visual_callback:
            visual_callback(closed_list)

        # Si llegamos a la meta, reconstruimos el camino
        if actual == meta:
            return reconstruir(padres, actual, inicio)

        # Exploramos los vecinos (arriba, abajo, izquierda, derecha)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            vecino = (actual[0]+dx, actual[1]+dy)

            # Si el vecino está fuera de los límites, lo ignoramos
            if not (0 <= vecino[0] < n and 0 <= vecino[1] < n):
                continue
            # Si es un obstáculo o ya lo exploramos, lo ignoramos
            if matriz[vecino[1]][vecino[0]] == 1 or vecino in closed_list:
                continue

            # Calculamos g(n)
            nuevo_g = g[actual] + 1
            # Si es mejor camino o aún no está en open_list
            if vecino not in open_list or nuevo_g < g.get(vecino, float('inf')):
                padres[vecino] = actual
                g[vecino] = nuevo_g
                f[vecino] = nuevo_g + heuristica(vecino, meta)
                if vecino not in open_list:
                    open_list.append(vecino)

    return []  # Si no se encuentra camino

# Función para reconstruir el camino desde meta hasta inicio
def reconstruir(padres, actual, inicio):
    camino = []
    while actual in padres:
        camino.append(actual)
        actual = padres[actual]
    camino.append(inicio)
    camino.reverse()
    return camino
