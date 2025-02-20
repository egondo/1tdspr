palavra = input("Informe uma palavra: ")

contagem = {}

for letra in palavra:
    #print(letra)
    if letra in contagem:
        contagem[letra] = contagem[letra] + 1
    else:
        contagem[letra] = 1

#print(contagem)
for c in contagem:
    print(f'{c} -> {contagem[c]}')