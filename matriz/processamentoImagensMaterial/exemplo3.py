import Imagem as img

dados = img.getMatrizImagemColorida("lago_canada.jpg")

matriz_red = dados[0]
matriz_green = dados[1]
matriz_blue = dados[2]

img.salvaImagemColorida("lago_alterado.jpg", matriz_blue, matriz_red, matriz_green)

for lin in matriz_red:
    print(lin)
print("Imagem gerada com sucessso")