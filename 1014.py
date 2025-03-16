def consumo_por_litro(x,y):
    consumo = x/y
    return consumo

quilometros = int(input())
litros = float(input())

consumo_medio = quilometros/litros

print(f"{consumo_medio:.3f} km/l")