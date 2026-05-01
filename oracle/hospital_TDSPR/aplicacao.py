import negocio

def menu() -> int:
    print("HOSPITAL TDSPR")
    print("1 - Senha")
    print("2 - Triagem")
    print("3 - Abertura Ficha")
    print("4 - Consulta Médica")
    print("5 - Atendimento") #medicacao, rx, ultrasom, etc
    print("6 - Alta hospitalar")
    print("10 - Sair")
    return int(input("Escolha: "))

def colhe_dados_triagem():
    pressao = input("Pressao: ")
    batimento = int(input("Batimento: "))
    temperatura = float(input("Temperatura: "))
    altura = float(input("Altura (m): "))
    peso = int(input("Peso: "))
    sintomas = input("Sintomas: ")
    resp = {"pressao": pressao, "batimento": batimento, "temperatura": temperatura, "altura": altura, "peso": peso, "func_id_fk": 1, "sintomas": sintomas}
    return resp

def colhe_dados_paciente(pac: dict):
    nome = input(f"Nome ({pac['nome']}): ")
    if len(nome) > 0:
        pac['nome'] = nome

    cpf = input(f"CPF: ({pac['cpf']}): ")
    if len(cpf) > 0:
        pac['cpf'] = cpf

    nasc = input(f"Nascimento ({pac['nascimento']}): ")
    if len(nasc) > 0:
        pac['nascimento'] = nasc

    conv = input(f"Convenio ({pac['convenio']}): ")
    if len(conv) > 0:
        pac['convenio'] = conv


opcao = menu()
while opcao != 6:
    if opcao == 1:
        nome = input("Nome: ")
        cpf = input("Cpf: ")
        senha = negocio.pega_senha_totem(nome, cpf)
        print(f"Senha: {senha}")
    
    elif opcao == 2:
        senha = int(input("Senha: "))
        tri = colhe_dados_triagem()
        negocio.grava_triagem(tri, senha)
        print("Triagem inserida com sucesso!")
    
    elif opcao == 3:
        senha = int(input("Senha: "))
        pac = negocio.rec_paciente_senha(senha)
        colhe_dados_paciente(pac)
        negocio.atualiza_paciente_recepcao(pac)
        print("Paciente atualizado com sucesso!")

    elif opcao == 4:
        senha = int(input("Senha: "))
        desc = input("Descricao da consulta: ")
        pront = {"descricao": "consulta médica", "observacao": desc, "func_id_fk": 21}
        negocio.grava_prontuario(pront, senha)
        print("Prontuario gravado com sucesso!")

    opcao = menu()