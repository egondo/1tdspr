import hashlib

def cadastra_usuario(nome, email, senha):
    with open("usuario.dat", mode="a") as arq:
        arq.write(f"{nome}:{email}:{hash(senha)}\n")

def hash(valor: str) -> str:
    hash_object = hashlib.md5(valor.encode('utf-8'))
    return hash_object.hexdigest()
    
#base = [
#    ['profeduardo@fiap.com.br', 'abr4e3473243f'],
#    ['profkarina@fiap.com.br', '52298abc539']
#]

def autentica(email, senha, base: list) -> bool:
    senha_hash = hash(senha)
    for info in base:
        if info[0] == email and info[1] == senha_hash:
            return True
    return False

def leitura_base_usuarios() -> list:
    arq = open('usuario.dat', mode="r")
    resp = []
    for info in arq:
        dados = info.strip().split(":")
        resp.append([dados[1], dados[2]])
    arq.close()
    return resp

opcao = 0
while opcao != 3:
    print("1 - cadastra\n2 - autentica\n3 - sair")
    opcao = int(input("escolha: "))
    if opcao == 1:
        nome = input("Informe o nome: ")
        email = input("Email: ")
        senha = input("senha: ")
        cadastra_usuario(nome, email, senha)
    elif opcao == 2:
        base = leitura_base_usuarios()
        email = input("Email: ")
        senha = input("Senha: ")
        if autentica(email, senha, base):
            print("Autenticado com sucesso!")
        else:
            print("Email ou senha invalidos")

print("Saindo do sistema")