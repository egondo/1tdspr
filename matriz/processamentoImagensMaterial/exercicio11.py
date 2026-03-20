import Imagem as img

dados = img.getMatrizImagemColorida("naturezaMorta.jpg")
red = dados[0]
green = dados[1]
blue = dados[2]

#criar uma matriz para armazenar os pixels cinzas
lin = len(red)
col = len(red[0])

grey = []
for i in range(lin):
    grey.append([0] * col)

#transformacao da imagem colorida para tons de cinza
for i in range(lin):
    for j in range(col):
        grey[i][j] = int((red[i][j] + green[i][j] + blue[i][j]) / 3)

img.salvaImagemCinza("natureza_cinza2.jpg", grey)            