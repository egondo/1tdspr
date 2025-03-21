def criacao() -> list:
    lista = []
    lista.append([0] * 5)
    lista.append([0] * 5)
    lista.append([0] * 5)
    lista.append([0] * 5)
    return lista

def criacao2() -> list:
    lista = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    return lista

def imprime(mat):
    for lin in mat:
        print(lin)

if __name__ == "__main__":
    matriz = criacao()
    #matriz[0][0] = 1
    #matriz[0][1] = 2
    #matriz[0][2] = 3
    #matriz[0][3] = 4
    #matriz[0][4] = 5
    num = 1
    for i in range(4):
        for j in range(5):
            matriz[i][j] = num
            num = num + 1

    imprime(matriz)