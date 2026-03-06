def soma_pos(matriz: list) -> int:
    #dimensoes da matriz
    lin = len(matriz)
    col = len(matriz[0])

    soma = 0
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] > 0:
                soma = soma + matriz[i][j]
    return soma


mat = [[-2, 4, 5, 0, -4], [-5, 6, 2, 9, 0], [-8, 4, 1, 0, 2]]
resultado = soma_pos(mat)
print(resultado)