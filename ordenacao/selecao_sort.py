def menor(lista: list, pos: int) -> int:
    pos_menor = pos
    while pos < len(lista):
        if lista[pos_menor] > lista[pos]:
            pos_menor = pos
        pos = pos + 1
    return pos_menor


def ordena(lista: list):
    for i in range(len(lista) - 1):
        p = menor(lista, i)
        aux = conjunto[p]
        conjunto[p] = conjunto[i]
        conjunto[i] = aux

conjunto = [3, 7, -2, 4, 0, 1, -8]
ordena(conjunto)
print(conjunto)