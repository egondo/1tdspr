import Imagem as img

matriz = img.getMatrizImagemCinza("wallpaper.png")

lin = len(matriz)
col = len(matriz[0])

print(f"{col} X {lin}")

for i in range(lin):
    for j in range(col):
        matriz[i][j] = min(matriz[i][j] + 40, 255)

img.salvaImagemCinza("wallpaper_claro.png", matriz)
print("Imagem salva com sucesso!")