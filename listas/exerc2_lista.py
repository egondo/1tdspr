import random

def gera_numeros(n: int) -> list:
    lista = []
    while n > 0:
        lista.append(random.randint(1, 1001))
        n = n - 1
    return lista


lst = gera_numeros(20)
print(lst)