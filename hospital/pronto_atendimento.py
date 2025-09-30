print("BEM VINDO ao HOSPITAL CURA CERTA")
contador = 1
sintomas = ""
opcao = 0

while opcao != 6:
    print("============= MENU ==========")
    print("1 - retirada de senha")
    print("2 - triagem")
    print("3 - cadastro de paciente")
    print("4 - consulta")
    print("5 - medicação")
    print("6 - sair")
    opcao = int(input("Informe uma opção: "))

    if opcao == 1:
        print(f"A sua senha é {contador}")
        contador = contador + 1
    elif opcao == 2:
        senha = int(input("Informe a senha: "))
        pressao = input("Pressão: ")
        saturacao = float(input("Saturação: "))
        temperatura = float(input("Temperatura: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
        bpm = int(input("BPM: "))
        sintomas = input("Sintomas: ")
    elif opcao == 3:
        senha = int(input("Informe a senha: "))
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")
        convenio = input("Convênio: ")
    elif opcao == 4:
        identificacao = int(input("ID do paciente (pulseira): "))
        sintomas = sintomas + input("Descreva mais sintomas do paciente: ")
        diagnostico = input("Qual é o diagnóstico: ")
    elif opcao == 6:
        print("Volte sempre! Mandaremos uma pesquisa de satisfação pelo Whatsapp")    
    else:
        print("Opção inválida, digite um número de 1 a 6!")