def maior(conjunto: list) -> int:
    pos_maior = 0
    i = 1
    
    while i < len(conjunto): 
        if conjunto[i] > conjunto[pos_maior]:
            pos_maior = i
        i = i + 1
    return pos_maior


lista = [35.6, 27.8, 42.9, 8.6, 52.9, 17.1]
pos = maior(lista)
print(pos) 






