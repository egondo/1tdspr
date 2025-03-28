import Imagem

dados = Imagem.getMatrizImagemColorida('lago_canada.jpg')

matriz_red = dados[0]
matriz_green = dados[1]
matriz_blue = dados[2]

#Criar uma outra matriz com as mesmas dimensoes do lago do Canada
lin = len(matriz_red)
col = len(matriz_red[0])

matriz_grey = []
for i in range(lin):
    matriz_grey.append([0] * col)

for i in range(lin):
    for j in range(col):
        soma = matriz_red[i][j] + matriz_green[i][j] + matriz_blue[i][j]
        matriz_grey[i][j] = int(soma / 3)

Imagem.salvaImagemCinza('lago_canada_cinza.jpg', matriz_grey)