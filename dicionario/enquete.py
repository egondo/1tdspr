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

while opcao != 6:
    opcao = menu()
    if opcao == 1:
        num = len(perguntas) + 1
        questao = cria_pergunta(num)
        perguntas.append(questao)
    
    elif opcao == 2 or opcao == 3:
        print("UNDER CONSTRUCTION")
    
    elif opcao == 4:
        for perg in perguntas:
            texto = formata(perg)
            print(texto)

    elif opcao == 5:
        print("Aplicando as perguntas")

    elif opcao == 6:
        print("Saindo do sistema, nenhuma informação será gravada")

    else:
        print("Opcao invalida")