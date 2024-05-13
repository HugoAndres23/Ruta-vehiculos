import requests
import networkx as nx
import aiohttp

async def obtener_distancia(origen, destino):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origen}&destinations={destino}&key=AIzaSyCawvsZQMZZOfRViEXQKEWqOH7O1rhR7Rw"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data["status"] == "OK":
                distancia = data["rows"][0]["elements"][0]["distance"]["value"]
                return distancia
            else:
                raise ValueError("Error al obtener la distancia desde la API de Google Maps.")


def calcular_ruta_mas_corta(origen, destinos):
    grafo = nx.Graph()
    for destino, distancia in destinos.items():
        grafo.add_edge(origen, destino, distancia=distancia)
        grafo.add_edge(destino, origen, distancia=distancia) 

    ruta = [origen]
    while len(ruta) < len(destinos) + 1:
        nodo_actual = ruta[0]
        distancia_minima = float("inf")
        nodo_siguiente = None
        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in ruta: 
                distancia = grafo[nodo_actual][vecino]["distancia"]
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    nodo_siguiente = vecino
        ruta.append(nodo_siguiente)

    return ruta
