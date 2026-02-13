import random

def embaralha(pedras: list):
    for i in range(0, len(pedras)):
        j = random.randint(0, len(pedras) - 1)
        aux = pedras[i]
        pedras[i] = pedras[j]
        pedras[j] = aux


def cria() -> list:
    monte = []
    for valor1 in range(0, 7):
        for valor2 in range(0, 7):
            monte.append([valor1, valor2])

    return monte

def compra(pedras: list) -> list:
    if len(pedras) > 0:
        return pedras.pop()
    else:
        return None   #equivale ao null do Java
    

def busca(conjunto: list, esq: int, dir: int) -> int:
    for i in range(len(conjunto)):
        p = conjunto[i]
        if p[0] == esq or p[1] == esq:
            return i
        elif p[0] == dir or p[1] == dir:
            return i
    return -1