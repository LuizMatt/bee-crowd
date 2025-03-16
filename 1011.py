def calcular_volume(raio):
    pi = 3.14159
    return (4 / 3) * pi * raio ** 3

raio = float(input())
volume = calcular_volume(raio)
print(f"VOLUME = {volume:.3f}")
