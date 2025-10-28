def menu() -> int:
    print("SISTEMA ENQUETE")
    print("1 - insere pergunta")
    print("2 - altera pergunta")
    print("3 - exclui pergunta")
    print("4 - lista perguntas")
    print("5 - aplicar enquete")
    print("6 - sair")
    opcao = int(input("Selecione: "))
    return opcao


def cria_pergunta(num: int) -> dict:
    num_aux = input(f"Q{num}, digite outro numero ou enter: ")
    if num_aux:
        num = int(num_aux)
    texto = input("enunciado: ")
    tipo = input("Tipo (ABERTA, UNICA, MULTIPLA): ")
    opcoes = []
    if tipo != "ABERTA":
        item = input("Alternativa (ou enter para encerrar): ")
        while item != '':
            opcoes.append(item)
            item = input("Alternativa (ou enter para encerrar): ")
    perg = {"num": num, "texto": texto, "tipo": tipo, "itens": opcoes}
    return perg

def formata(p: dict) -> str:
    resp = f"{p['num']}) {p['texto']}"
    if p['tipo'] != 'ABERTA':
        for item in p['itens']:
            resp = resp + f"\n{item}"

    return resp

#Programa principal
opcao = 0
perguntas = []
banco_respostas = []

while opcao != 6:
    opcao = menu()
    if opcao == 1:
        num = len(perguntas) + 1
        questao = cria_pergunta(num)
        perguntas.append(questao)
    
    elif opcao == 2:
        print("Altera Pergunta:")
        perg = cria_pergunta(0)
        i = 0
        alterado = False
        while i < len(perguntas):
            q = perguntas[i]
            if q['num'] == perg['num']:
                perguntas[i] = perg
                alterado = True
            i = i + 1
        if alterado:
            print("Pergunta alterada com sucesso!")
        else:
            print("Não foi possível alterar a pergunta")
    
    elif opcao == 4:
        for perg in perguntas:
            texto = formata(perg)
            print(texto)

    elif opcao == 5:
        print("Aplicando as perguntas")
        for perg in perguntas:
            texto = formata(perg)
            print(texto)
            resposta = input("Resposta: ")
            info = {"pergunta": perg, "resposta": resposta}
            banco_respostas.append(info)

    elif opcao == 6:
        print("Saindo do sistema, nenhuma informação será gravada")

    elif opcao == 7:
        print("Exibindo as respostas dadas: ")
        for registro in banco_respostas:
            perg = registro['pergunta']
            resp = registro['resposta']
            print(f"{perg['texto']} -> {resp}")
    else:
        print("Opcao invalida")