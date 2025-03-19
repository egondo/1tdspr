def soma(matriz_a: list, matriz_b: list) -> list:
    #so posso somar se as matrizes a e b tiverem 
    #as mesmas dimensões
    lin_a = len(matriz_a)
    col_a = len(matriz_a[0])
    lin_b = len(matriz_b)
    col_b = len(matriz_b[0])

    if lin_a != lin_b or col_a != col_b:
        raise Exception("Matrizes com dimensões diferentes")
    
    #crio a matriz resultado
    result = []
    for i in range(lin_a):
        result.append([0] * col_a)

    for i in range(lin_a):
        for j in range(col_a):
            result[i][j] = matriz_a[i][j] + matriz_b[i][j]
    
    return result


if __name__ == "__main__":
    a = [
        [2, 4, 7],
        [-3, 5, -2],
        [0, 2, 0]
    ]

    b = [
        [1, 7, 0],
        [2, 2, -7]
    ]

    mat = soma(a, b)
    print(mat)



