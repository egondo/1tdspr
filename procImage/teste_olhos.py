import Imagem

matriz = Imagem.getMatrizImagemCinza("wallpaper.png")

lin = len(matriz)
col = len(matriz[0])

print(f"{col} x {lin}")

for i in range(lin):
    for j in range(col):
        matriz[i][j] = matriz[i][j] - 50

Imagem.salvaImagemCinza('wall_escuro.png', matriz)
