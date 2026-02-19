import random

def embaralha(baralho: list):
    for i in range(0, len(baralho)):
        j = random.randint(0, len(baralho) - 1)
        aux = baralho[i]
        baralho[i] = baralho[j]
        baralho[j] = aux


def cria_truco() -> list:
    deck = cria()
    #removendo as cartas 8, 9 e 10 
    i = 0 
    while i < len(deck):
        carta = deck[i]
        if carta[0] >= 8 and carta[0] <= 10:
            deck.pop(i)
        else:
            i = i + 1
    return deck

def cria() -> list:
    monte = []
    for valor in range(1, 14):
        monte.append([valor, 'ouros'])
        monte.append([valor, 'espadas'])
        monte.append([valor, 'copas'])
        monte.append([valor, 'paus'])

    return monte
    #for valor in range(1, 14):
    #    for naipe in ['ouros', 'espadas', 'copas', 'paus']:
    #        monte.append([valor, naipe])

    #monte = [[valor, naipe] for valor in range(1, 14) for naipe in ['ouros', 'espadas', 'copas', 'paus']]

def compra(baralho: list) -> list:
    if len(baralho) > 0:
        return baralho.pop()
    else:
        return None   #equivale ao null do Java
    

def to_string(carta: list) -> str:
    valor = {1: "A", 11: "J", 12: "Q", 13: "K"}
    naipe = {"ouros": "♦", "copas": "♥", "espadas": "♠", "paus": "♣"}
    resp = ""
    if carta[0] == 1:
        resp = "A"
    elif carta[0] == 11:
        resp = "J"
    elif carta[0] == 12:
        resp = "Q"
    elif carta[0] == 13:
        resp = "K"
    else:
        resp = str(carta[0])
    
    if carta[1] == 'ouros':
        resp = resp + "♦" #alt + 4
    elif carta[1] == 'copas':
        resp = resp + "♥" #alt + 3
    elif carta[1] == 'paus':
        resp = resp + "♣" #alt + 5
    else:
         resp = resp + "♠" #alt + 6
    
    return resp


if __name__ == "__main__":
    monte = cria()
    embaralha(monte)

    carta = compra(monte)
    while carta != None:
        print(to_string(carta))
        carta = compra(monte)




