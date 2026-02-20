import time

def busca(lista: list, x: float) -> int:
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

def busca_bin(lista: list, x: float) -> int:
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] < x:
            ini = meio + 1
        elif lista[meio] > x:
            fim = meio - 1
        else:
            return meio

    return -1


lista = []
for i in range(20_000_000):
    lista.append(i + 10)

ini = time.time()
pos = busca(lista, 0)
fim = time.time()
print(f"Tempo busca simples {fim - ini}")

ini = time.time()
pos = busca_bin(lista, 0)
fim = time.time()
print(f"Tempo busca binaria {fim - ini}")

