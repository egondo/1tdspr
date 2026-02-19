import baralho

def get_valor(carta: list) -> int:
    if carta[0] == 3:
        return 30
    elif carta[0] == 2:
        return 20
    elif carta[0] == 1:
        return 15
    elif carta[0] == 11:
        return 12
    elif carta[0] == 12:
        return 11
    else:
        return carta[0]

def jogada_cpu(mao: list) -> list:
    return mao.pop()

def jogada_hum(mao: list) -> list:
    cartas = ""
    for c in mao:
        cartas = cartas + baralho.to_string(c)
    print(cartas)
    pos = int(input("Informe a posicao da carta: "))
    return mao.pop(pos)


rodada_hum = 0
rodada_cpu = 0

while rodada_cpu < 12 and rodada_hum < 12:
    deck = baralho.cria_truco()
    baralho.embaralha(deck)
    mao_hum = []
    mao_cpu = []
    for i in range(3):
        mao_hum.append(baralho.compra(deck))
        mao_cpu.append(baralho.compra(deck))

    pontos_hum = 0
    pontos_cpu = 0

    while pontos_cpu < 2 and pontos_hum < 2:
        c_hum = jogada_hum(mao_hum)
        c_cpu = jogada_cpu(mao_cpu)
        
        print("Mesa: ", baralho.to_string(c_hum), baralho.to_string(c_cpu))
        if get_valor(c_hum) > get_valor(c_cpu):
            pontos_hum = pontos_hum + 1
        elif get_valor(c_hum) < get_valor(c_cpu):
            pontos_cpu = pontos_cpu + 1
        else:
            pontos_cpu = pontos_cpu + 1
            pontos_hum = pontos_hum + 1

    if pontos_cpu > pontos_hum:
        rodada_cpu = rodada_cpu + 1
        print("Cpu ganhou a rodada")
    elif pontos_cpu < pontos_hum:
        rodada_hum = rodada_hum + 1
        print("Humano ganhou a rodada")

    print(f"CPU: {rodada_cpu} X Hum: {rodada_hum}")

