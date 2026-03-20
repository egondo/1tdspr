import Imagem as img

def escurece(mat: list):
    lin = len(mat)
    col = len(mat[0]) // 2
    for i in range(lin):
        for j in range(col + 1):
            mat[i][j] = max(mat[i][j] - 50, 0)

dados = img.getMatrizImagemColorida("lago_canada.jpg")

verm = dados[0]
verd = dados[1]
azul = dados[2]

escurece(verm)
escurece(verd)
escurece(azul)

img.salvaImagemColorida("lago_escurecido.jpg", verm, verd, azul)
print("imagem escurecida")
