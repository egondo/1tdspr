def ordena(lista: list):
    for i in range(len(lista)):
        subir(lista, i)


def subir(lista: list, j: int):
    pos = len(lista) - 1
    while pos > j:
        if lista[pos] < lista[pos-1]:
            aux = lista[pos]
            lista[pos] = lista[pos-1]
            lista[pos-1] = aux  
        pos = pos - 1

conj = [2, -7, 19, 6, 1, 75, 23, 45, 78, 62]
ordena(conj)
print(conj)