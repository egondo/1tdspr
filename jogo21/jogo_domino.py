import domino

def escolhe_pedra(pedras: list, esq: int, dir: int) -> list:
    print(f"Esq: {esq}, Dir: {dir}")
    aux = ''
    for i in range(len(pedras_hum)):
        aux = f"{aux} {pedras_hum[i]}"
    print(aux)
    pos = int(input("Digite uma posicao que deseja jogar"))
    return pedras.pop(pos)
    

pedras = domino.cria()
domino.embaralha(pedras)

pedras_hum = []
pedras_cpu = []
for i in range(14):
    pedras_hum.append(domino.compra(pedras))
    pedras_cpu.append(domino.compra(pedras))

mesa = []
pedra = escolhe_pedra(pedras_hum, 0, 0)
mesa.append(pedra)
esq = pedra[0]
dir = pedra[1]
vez_humano = False

while len(pedras_hum) > 0 and len(pedras_cpu) > 0:
    
    print(mesa)

    if vez_humano:
        pedra = escolhe_pedra(pedras_hum, esq, dir)
        if pedra[0] == esq:
            mesa.insert(0, pedra)
            esq = pedra[1]
        elif pedra[1] == esq:
            mesa.insert(0, pedra)
            esq = pedra[0]    
        elif pedra[0] == dir:
            mesa.append(pedra)
            dir = pedra[1]
        elif pedra[1] == dir:
            mesa.append(pedra)
            dir = pedra[0]    
        vez_humano = False        

    else:
        pos = domino.busca(pedras_cpu, esq, dir)
        if pos != -1:
            pedra = pedras_cpu.pop(pos)
            if pedra[0] == esq:
                mesa.insert(0, pedra)
                esq = pedra[1]
            elif pedra[1] == esq:
                mesa.insert(0, pedra)
                esq = pedra[0]    
            elif pedra[0] == dir:
                mesa.append(pedra)
                dir = pedra[1]
            elif pedra[1] == dir:
                mesa.append(pedra)
                dir = pedra[0]    
        vez_humano = True