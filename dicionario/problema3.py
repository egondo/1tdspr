def inclui(conj: list):
    print("Inclui Produto: ")
    codigo = int(input("Código: "))
    desc = input("Descrição: ")
    qtd = int(input("Quantidade: "))
    prc = float(input("Preço: "))

    prod = {'codigo': codigo, 'descricao': desc, 'quantidade': qtd, 'preco': prc}

    conj.append(prod)


def altera():
    pass

def consulta():
    pass

def exclui():
    pass

print("Sistema de cadastro de produtos: ")
opcao = 0
lista = []

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
        altera()
    elif opcao == 3:
        consulta()
    elif opcao == 4:
        exclui()


print(lista)