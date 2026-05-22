import os
import time

def encontra_vizinhos_nao_visitados(pos: tuple, maze: list, valor: int) -> list:
    resp = []
    l = pos[0]
    c = pos[1]
    ind_last_col = len(maze[0]) - 1
    ind_last_lin = len(maze) - 1

    #norte
    if l > 0 and maze[l - 1][c] == 0:
        maze[l-1][c] = valor
        resp.append( (l-1, c) )

    #leste
    if c < ind_last_col and maze[l][c + 1] == 0:
        maze[l][c+1] = valor
        resp.append( (l, c+1) )

    #sul
    if l < ind_last_lin and maze[l + 1][c] == 0:
        maze[l+1][c] = valor
        resp.append( (l+1, c) )

    #oeste
    if c > 0 and maze[l][c - 1] == 0:
        maze[l][c-1] = valor
        resp.append( (l, c-1) )

    return resp

def imprime(maze):
    for row in maze:
        print(row)


labirinto = [
    [ 0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0],
    [ 0, -1,  0,  0, -1,  0, -1,  0, -1, -1,  0],
    [ 0,  0, -1,  0, -1,  0, -1,  0,  0,  0, -1],
    [ 0, -1,  0, -1,  0,  0,  0, -1, -1,  0,  0],
    [ 0,  0,  0, -1,  0, -1,  0,  0,  0, -1,  0],
    [ 0, -1,  0,  0,  0,  0,  0,  0, -1,  0,  0]]

#inicializacao
pos = (5, 10)
labirinto[5][10] = 1
fila = []
fila.append(pos)

while pos != (0, 0):
    pos = fila.pop(0)
    l = pos[0]
    c = pos[1]
    valor = labirinto[l][c] + 1
    vizinhos = encontra_vizinhos_nao_visitados(pos, labirinto, valor)
    for coordenada in vizinhos:
        fila.append(coordenada)
    os.system('clear') #cls
    imprime(labirinto)
    time.sleep(0.8)

#a partir da matriz preenchida, tente encontrar o caminho que devemos percorrer para chegar na saída do labirintop (basta percorrer as posicoes da matriz partindo da posicao (0, 0) e procurando uma casa com valor um a menos do que a posição anterior.