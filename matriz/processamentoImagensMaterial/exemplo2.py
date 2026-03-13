import Imagem as img

domino = img.getMatrizImagemCinza("domino.png")

pedra = []
for i in range(37):
    pedra.append([0] * 70)

deltai = 12
deltaj = 12

for i in range(37):
    for j in range(70):
        pedra[i][j] = domino[i + deltai][j + deltaj]    

img.salvaImagemCinza("pedra.png", pedra)
print("Imagem salva com sucesso")