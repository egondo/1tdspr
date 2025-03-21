arq = open("dados_produto.txt", mode="r")
conteudo_inteiro = arq.read()
print(conteudo_inteiro)
arq.close()

with open("dados_produto.txt", mode="r") as arq:
    dados = arq.readlines()
    print(dados)