from pilha import Pilha
import os
import time

def cria_matriz() -> list:
    mat = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    return mat

def busca_posicao_imutavel(mat: list) -> dict:
    #procura na matriz todas as posicoes que armazenam valores
    #iniciais do jogo do Sudoku
    dic = {}
    for i in range(9):
        for j in range(9):
            if mat[i][j] != 0:
                dic[(i, j)] = (i, j)
    return dic

def proxima_posicao(pos: tuple) -> tuple:
    lin = pos[0]
    col = pos[1]
    if col == 8: #estou na coluna de indice 8
        return (lin+1, 0)
    else:
        return (lin, col+1)

def pode_linha(mat, lin, valor) -> bool:
    for j in range(9):
        if mat[lin][j] == valor:
            return False
    return True

def pode_coluna(mat, col, valor) -> bool:
    for i in range(9):
        if mat[i][col] == valor:
            return False
    return True

#Valida se pode colocar o valor na regiao da posicao (lin, col)
def pode_regiao(mat, lin, col, valor) -> bool:
    l = (lin // 3) * 3
    c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            #print("=>", (l+i, c+j))
            if mat[l+i][c+j] == valor:
                return False
    return True        

def coloquei(mat, lin, col, valor) -> bool:

    if pode_linha(mat, lin, valor) and pode_coluna(mat, col, valor) and pode_regiao(mat, lin, col, valor):
        mat[lin][col] = valor
        return True
    return False

def imprime(mat):
    for lin in mat:
        print(lin)

sud = cria_matriz()
pos = (0, 0)  #primeira posicao da matriz
pilha = Pilha(100)
posicao_inicial_sudoku = busca_posicao_imutavel(sud)

while pos != (9, 0):
    if pos in posicao_inicial_sudoku:
        pos = proxima_posicao(pos)
    else:
        lin = pos[0]
        col = pos[1]
        valor = sud[lin][col] + 1
        while not coloquei(sud, lin, col, valor) and valor < 10:
            #print("VL ",valor)
            valor = valor + 1

        if valor < 10: #consegui colocar o valor dentro do sudoku
            pilha.put(pos)
            pos = proxima_posicao(pos)
            
            os.system('cls')
            imprime(sud)
            time.sleep(0.1)

        else:
            sud[lin][col] = 0  #backtracking
            pos = pilha.pop()

imprime(sud)