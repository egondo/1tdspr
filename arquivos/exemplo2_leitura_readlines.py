arq = open("personagens.txt", mode="r")
lista = arq.readlines()
arq.close()

#for super_heroi in lista:
#    print(super_heroi.strip()) #removendo a quebra de linha do arquivo

for i in range(0, len(lista)):
    heroi = lista[i].strip()
    for j in range(i + 1, len(lista)):
        print(f"{heroi} vs {lista[j].strip()}\n")


