import Imagem as img

def rotaciona(mat: list) -> list:
    lin = len(mat)
    col = len(mat[0])
    resp = []
    for i in range(lin):
        resp.append([0] * col)
    #coluna
    #resp[lin - 1][col - 1 - 0] = mat[0][0]
    #resp[lin - 1][col - 1 - 1] = mat[0][1]
    #linha
    #resp[lin -1 - 1][col - 1 - 0] = mat[1][0]
    #resp[lin -1 - 2][col - 1 - 0] = mat[2][0]
    for i in range(lin):
        for j in range(col):
            resp[lin -1 - i][col - 1 - j] = mat[i][j]
    return resp

dados = img.getMatrizImagemColorida("lago_canada.jpg")

verm = dados[0]
verd = dados[1]
azul = dados[2]

verm_180 = rotaciona(verm)
verd_180 = rotaciona(verd)
azul_180 = rotaciona(azul)

img.salvaImagemColorida("lago_180.jpg", verm_180, verd_180, azul_180)
print("imagem rotacionada")
