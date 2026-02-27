def organiza(lista: list, i: int):
    #i = len(lista) - 1
    aux = lista[i]
    while i > 0 and lista[i-1] > aux:
        lista[i] = lista[i-1]
        i = i - 1
    
    lista[i] = aux


def ordena(lista: list):
    for i in range(1, len(lst)):
        organiza(lista, i)


#lst = [4, 6, 10, 23, 56, 57, 62, 62, 78, 18]
lst = [23, 9, 0, -3, 56, 12, 18, 62, 4, 19]
ordena(lst)
print(lst)    