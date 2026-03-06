import random
def filtro_black_white(matriz: list):
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] <= 127:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 255

if __name__ == "__main__":
    mat = []
    for i in range(800):
        mat.append([0] * 1200)
        for j in range(1200):
            mat[i][j] = random.randint(0, 255)
    
    filtro_black_white(mat)
    for lin in mat:
        print(lin)