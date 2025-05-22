from collections import deque
import time

# Mapa del desierto de Arrakis
grafo_arrakis = {
    "Arrakeen": ["Sietch Tabr", "Oasis del Norte", "Campamento Fremen"],
    "Sietch Tabr": ["Arrakeen", "Oasis del Este", "Montaña de la Especia"],
    "Oasis del Norte": ["Arrakeen", "Campamento Fremen"],
    "Campamento Fremen": ["Arrakeen", "Oasis del Norte", "Oasis del Este"],
    "Oasis del Este": ["Sietch Tabr", "Campamento Fremen", "Zona Peligrosa"],
    "Montaña de la Especia": ["Sietch Tabr", "Zona Peligrosa"],
    "Zona Peligrosa": ["Oasis del Este", "Montaña de la Especia"]
}

# Tarea 1: Ruta más corta hacia el Oasis del Norte (BFS)
def bfs_ruta_corta(grafo, origen, destino="Oasis del Norte"):
    visitados = set()
    cola = deque([(origen, [origen])])

    while cola:
        actual, ruta = cola.popleft()
        if actual == destino:
            print(f"Ruta más corta desde {origen} hasta {destino}: {' -> '.join(ruta)}")
            print(f"Distancia total: {len(ruta)} nodos")
            return ruta
        visitados.add(actual)
        for vecino in grafo[actual]:
            if vecino not in visitados and vecino not in [nodo for nodo, _ in cola]:
                cola.append((vecino, ruta + [vecino]))
    print("No se encontró una ruta.")
    return None

# Tarea 2: Verificar conectividad del grafo (DFS)
def dfs_conectividad(grafo, nodo_inicial, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo_inicial)
    for vecino in grafo[nodo_inicial]:
        if vecino not in visitados:
            dfs_conectividad(grafo, vecino, visitados)
    return visitados

def verificar_conectividad(grafo):
    visitados = dfs_conectividad(grafo, list(grafo.keys())[0])
    if len(visitados) == len(grafo):
        print("El grafo ES conexo.")
    else:
        print("El grafo NO es conexo.")

# Tarea 3: Rutas seguras hacia la Montaña de la Especia (sin Zona Peligrosa)
def bfs_rutas_seguras(grafo, origen, destino="Montaña de la Especia"):
    cola = deque([(origen, [origen])])
    rutas = []

    while cola:
        actual, ruta = cola.popleft()
        if actual == destino:
            rutas.append(ruta)
            continue
        for vecino in grafo[actual]:
            if vecino not in ruta and vecino != "Zona Peligrosa":
                cola.append((vecino, ruta + [vecino]))

    if rutas:
        print(f"Rutas seguras hacia {destino}:")
        for ruta in rutas:
            print(" -> ".join(ruta))
    else:
        print("No hay rutas seguras disponibles.")
    return rutas

# Tarea 4: Búsqueda de Melange con DFS
def dfs_melange(grafo, actual, visitados=None, orden=None):
    if visitados is None:
        visitados = set()
    if orden is None:
        orden = []

    visitados.add(actual)
    orden.append(actual)

    for vecino in grafo[actual]:
        if vecino not in visitados:
            dfs_melange(grafo, vecino, visitados, orden)
    return orden

# Tarea 5: Análisis de eficiencia
def medir_tiempos():
    print("\n⏱ Análisis de Eficiencia:\n")

    inicio = time.time()
    bfs_ruta_corta(grafo_arrakis, "Arrakeen")
    print("Tiempo BFS Ruta Corta:", round(time.time() - inicio, 6), "s")

    inicio = time.time()
    verificar_conectividad(grafo_arrakis)
    print("Tiempo DFS Conectividad:", round(time.time() - inicio, 6), "s")

    inicio = time.time()
    bfs_rutas_seguras(grafo_arrakis, "Arrakeen")
    print("Tiempo BFS Rutas Seguras:", round(time.time() - inicio, 6), "s")

    inicio = time.time()
    orden_dfs = dfs_melange(grafo_arrakis, "Arrakeen")
    print("Orden de exploración DFS (Melange):", " -> ".join(orden_dfs))
    print("Tiempo DFS Melange:", round(time.time() - inicio, 6), "s")

    print("\n🔍 Conclusión:")
    print(" BFS es mejor cuando se necesita la ruta más corta o evitar nodos peligrosos.")
    print(" DFS es útil para exploración completa y verificar si el grafo es conexo.")

# Ejecución principal
if __name__ == "__main__":
    bfs_ruta_corta(grafo_arrakis, "Arrakeen")
    verificar_conectividad(grafo_arrakis)
    bfs_rutas_seguras(grafo_arrakis, "Arrakeen")
    orden = dfs_melange(grafo_arrakis, "Arrakeen")
    print("\nOrden de exploración de Melange:", " -> ".join(orden))
    medir_tiempos()
