import baralho as deck

def calcula_pontuacao(mao: list) -> int:
    pontos = 0
    for c in mao:
        if c[0] > 10:   #valor da carta > 10
            pontos = pontos + 10
        else:
            pontos = pontos + c[0]
    return pontos

def quer_carta(mao: list) -> bool:
    saida = ""
    for c in mao:
        saida = f"{saida} {deck.to_string(c)}"
    
    pontos = calcula_pontuacao(mao)
    print(f"Cartas: {saida}")
    print(f"Pontos: {pontos}")
    resp = input("Quer mais carta (s/n): ")
    if resp == 'S' or resp == 's':
        return True
    else:
        return False


def quer_carta_cpu(mao: list) -> bool:
    pontos = calcula_pontuacao(mao)
    if pontos < 16:
        return True
    else:
        return False


monte = deck.cria()
deck.embaralha(monte)

mao_jog1 = []
mao_jog1.append(deck.compra(monte))
mao_jog1.append(deck.compra(monte))

mao_jog2 = []
mao_jog2.append(deck.compra(monte))
mao_jog2.append(deck.compra(monte))

while quer_carta(mao_jog1):
    c = deck.compra(monte)
    mao_jog1.append(c)

while quer_carta_cpu(mao_jog2):
    c = deck.compra(monte)
    mao_jog2.append(c)

print(f"Você fez {calcula_pontuacao(mao_jog1)}")
print(f"CPU fez {calcula_pontuacao(mao_jog2)}")




