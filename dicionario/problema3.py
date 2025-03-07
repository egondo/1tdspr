def inclui(conj: list):
    print("Inclui Produto: ")
    codigo = int(input("Código: "))
    desc = input("Descrição: ")
    qtd = int(input("Quantidade: "))
    prc = float(input("Preço: "))

    prod = {'codigo': codigo, 'descricao': desc, 'quantidade': qtd, 'preco': prc}

    conj.append(prod)


def altera(conj: list):
    cod = int(input("Informe o código do produto: "))
    produto = consulta(conj, cod)
    if len(produto) > 0:
        desc = input("Descrição: ")
        qtd = int(input("Quantidade: "))
        prc = float(input("Preço: "))
        produto['descricao'] = desc
        produto['quantidade'] = qtd
        produto['preco'] = prc
    else:
        print("Nenhum produto com o código fornecido!")

def consulta(conj: list, cod: int) -> dict:
    for prod in conj:
        if prod["codigo"] == cod:
            return prod
    return {}

def exclui(conj: list):
    cod = int(input("Informe o código do produto: "))
    i = 0
    removido = False
    while i < len(conj) and not removido:
        prod = conj[i]
        if prod['codigo'] == cod:
            conj.pop(i)
            removido = True
        i = i + 1

    if removido:
        print("Produto removido com sucesso!")
    else:
        print("Produto nao enontrado")

def gravar_dados(conj: list):
    with open("dados_produto.txt", mode="w", encoding="utf8") as arq:
        for prod in conj:
            cod = prod['codigo']
            desc = prod['descricao']
            qtd = prod['quantidade']
            prc = prod['preco'] 
            arq.write(f"{cod};{desc};{qtd};{prc}\n")

def ler_dados() -> list:
    resp = []
    with open("dados_produto.txt", mode="r", encoding="utf8") as arq:
        linhas = arq.readlines()
        for reg in linhas:
            campos = reg.split(";")
            prod = {
                "codigo": int(campos[0]), 
                "descricao": campos[1],
                "quantidade": int(campos[2]),
                "preco": float(campos[3])
            }
            resp.append(prod)
    return resp

print("Sistema de cadastro de produtos: ") 
opcao = 0
lista = ler_dados()

while opcao != 5:
    print('1 - inclui')
    print('2 - altera')
    print('3 - consulta')
    print('4 - exclui')
    print('5 - sair')
    opcao = int(input('Selecione a opção desejada: '))
    if opcao == 1:
        inclui(lista)
    elif opcao == 2:
        altera(lista)
    elif opcao == 3:
        cod = int(input("Código: "))
        prod = consulta(lista, cod)
        if len(prod) > 0:
            print(prod)
        else:
            print("Produto não encontrado")
    elif opcao == 4:
        exclui(lista)


#print(lista)
gravar_dados(lista)