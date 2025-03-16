def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


def area_circulo(raio):
    area = (raio ** 2) * 3.14159
    return area


def area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area


def area_quadrado(lado):
    area = lado ** 2
    return area


def area_retangulo(lado_a, lado_b):
    area = lado_a * lado_b
    return area


a, b, c = map(float, input().split())

triangulo = area_triangulo(a, c)
circulo = area_circulo(c)
trapezio = area_trapezio(a, b, c)
quadrado = area_quadrado(b)
retangulo = area_retangulo(a, b)

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
