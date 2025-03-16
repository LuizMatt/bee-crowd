import math


def distancia_entre_pontos(x1, x2, y1, y2):
    distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distancia


a, c = map(float, input().split())
b, d = map(float, input().split())
calculo_distancia = float(distancia_entre_pontos(a, b, c, d))
print(f"{calculo_distancia:.4f}")
