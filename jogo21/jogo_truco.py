import baralho as bar

def sucessor(carta: list) -> int:
    if carta[0] == 7:
        return 12
    elif carta[0] == 12:
        return 11
    elif carta[0] == 11:
        return 13
    elif carta[0] == 13:
        return 1
    else:
        return carta[0] + 1

def get_valor(carta: list, vira: list) -> int:
    valor_manilha = sucessor(vira)
    if carta[0] == valor_manilha:
        if carta[1] == 'paus':
            return 400
        elif carta[1] == 'copas':
            return 300
        elif carta[1] == 'espadas':
            return 200
        else:
            return 100
    elif carta[0] == 3:
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

def jogada_hum(mao: list, c: list) -> list:
    if c != None:
        print(f"CPU -> {bar.to_string(c)}")
    cartas = ""
    for c in mao:
        cartas = cartas + bar.to_string(c)
    print(cartas)
    pos = int(input("Informe a posicao da carta: "))
    return mao.pop(pos)


def distribui(deck: list):
    mao_c = []
    mao_h = []
    for i in range(3):
        mao_h.append(bar.compra(deck))
        mao_c.append(bar.compra(deck))
    return mao_h, mao_c


#5) idem para a jogada da cpu

rodada_hum = 0
rodada_cpu = 0
rodada = 0

while rodada_cpu < 12 and rodada_hum < 12:
    deck = bar.cria_truco()
    bar.embaralha(deck)
    bar.embaralha(deck)
    
    mao_hum, mao_cpu = distribui(deck)
    vira = bar.compra(deck)
    print(f"Vira {bar.to_string(vira)}")
    pontos_hum = 0
    pontos_cpu = 0

    vez_hum = True
    if rodada % 2 == 1:
        vez_hum = False
    rodada = rodada + 1
    while pontos_cpu < 2 and pontos_hum < 2:
        if vez_hum:
            c_hum = jogada_hum(mao_hum, None)
            c_cpu = jogada_cpu(mao_cpu)
        else:
            c_cpu = jogada_cpu(mao_cpu)
            c_hum = jogada_hum(mao_hum, c_cpu)
        
        print("Mesa: ", bar.to_string(c_hum), bar.to_string(c_cpu))
        valor_h = get_valor(c_hum, vira)
        valor_c = get_valor(c_cpu, vira)
        if valor_h > valor_c:
            pontos_hum = pontos_hum + 1
            vez_hum = True
        elif valor_h < valor_c:
            pontos_cpu = pontos_cpu + 1
            vez_hum = False
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

