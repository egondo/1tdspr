import json

def menu() -> int:
    print("1 Consulta")
    print("2 Cadastra")
    print("3 Sair")
    return int(input("Opcao: "))

def consulta(banco: dict):
    chave = input("Chave PIX: ")
    if chave in banco:
        print(banco[chave])
    else:
        print(f"Não existe {chave} cadastrada no PIX!")


def cadastra(banco: dict):
    chave = input("Chave PIX: ")
    if chave in banco:
        print(f"Chave PIX {chave} já consta no sistema!")
    else:
        nome = input("Nome: ")
        nome_banco = input("Banco: ")
        conta = input("Conta: ")
        info = {"nome": nome, "banco": nome_banco, "conta": conta}
        banco[chave] = info


def leitura_arquivo() -> dict:
    try:
        arq = open("banco_pix.dat", mode="r", encoding="utf8")
        return json.load(arq)
    except:
        return {}

def gravacao_arquivo(banco: dict):
    arq = open("banco_pix.dat", mode="w", encoding="utf8")
    json.dump(banco, arq)

if __name__ == "__main__":
    print("Sistema PIX")
    op = menu()
    
    banco_chaves = leitura_arquivo()

    while op != 3:
        if op == 1:
            consulta(banco_chaves)
        elif op == 2:
            cadastra(banco_chaves)
        elif op != 3:
            print("Opcao inválida!")
        op = menu()

    gravacao_arquivo(banco_chaves)