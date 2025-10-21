def inverte(lista: list) -> None:
    i = 0
    j = len(lista) - 1 #j armazena o último indice da lista

    while i < j:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
        i = i + 1
        j = j - 1

frutas = ["uva", "jaca", "maca", "amora", "pera", "coco", "lichia"]
inverte(frutas)
print(frutas)
