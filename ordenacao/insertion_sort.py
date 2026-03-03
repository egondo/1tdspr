#recebe uma lista praticamente ordenada
#apenas o último elemento está fora de lugar
def organiza(lista: list, i: int):
    #i = len(lista) - 1
    valor = lista[i]
    while i > 0 and valor < lista[i-1]:
        lista[i] = lista[i-1]
        i = i - 1
    lista[i] = valor

lst = [4, 1, -8, 16, 10, 3, 2, 7, 15]
organiza(lst, 1)
organiza(lst, 2)
organiza(lst, 3)

print(lst)