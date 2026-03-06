def esta_ordenado(lista: list) -> bool:
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            return False
        i = i + 1
    return True

l = [1, 3, 9, 10, 12, 10, 18, 18, 23]
print(esta_ordenado(l))
