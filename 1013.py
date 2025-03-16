def encontrar_maior(a, b, c):
    maior_ab = int((a + b + abs(a - b)) / 2)
    maior_abc = int((maior_ab + c + abs(maior_ab - c)) / 2)
    return maior_abc


a, b, c = map(int, input().split())

maior_valor = encontrar_maior(a, b, c)
print(f"{maior_valor} eh o maior")
