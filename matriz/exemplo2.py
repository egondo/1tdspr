def soma(mat_a, mat_b) -> list:
    #criar a matriz resultado
    resultado = []
    lin = len(mat_a)
    col = len(mat_a[0])
    i = 0
    while i < lin:
        resultado.append([0] * col)
        i = i + 1

    #para cada elemento da mat_a somo com o seu correspondente
    #da mat_b e coloco na posicao correspondente da matriz resultado
    for i in range(lin):
        for j in range(col):
            resultado[i][j] = mat_a[i][j] + mat_b[i][j]
    return resultado