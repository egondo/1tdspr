arq = open("dados_2.txt", "r")

for linha in arq:
    print(linha.strip())

arq.close()