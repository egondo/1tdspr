import random

def cria_matriz() -> list:
    #criar a matriz 5x7
    mat = []
    for i in range(5):
        mat.append([0] * 7)

    for i in range(5):
        for j in range(7):
            mat[i][j] = random.randint(0, 1000)
    return mat