def analisa_partida(partida: str) -> list:
    partida = partida.replace("\n", "")
    aux = partida.split(" X ")
    time_a = aux[0]
    pos = len(time_a) - 1
    gol_a = time_a[pos]
    time_a = time_a[0:pos-1]

    time_b = aux[1]
    gol_b = time_b[0]
    time_b = time_b[2:] #extrai a substring a partir da pos 2 ate o fim

    return [time_a, int(gol_a), time_b, int(gol_b)]


def atribui_valor_time(nome: str, valor: int, tabela: dict):
    if nome in tabela:
        tabela[nome] = tabela[nome] + valor
    else:
        tabela[nome] = valor    

arquivo = open("arquivos/jogos.txt", mode="r", encoding="utf8")

lista = arquivo.readlines()
tabela = {}

for jogo in lista:
    #print(analisa_partida(jogo))
    info = analisa_partida(jogo)
    time_a = info[0]
    time_b = info[2]    

    if info[1] > info[3]:
        atribui_valor_time(time_a, 3, tabela)
        atribui_valor_time(time_b, 0, tabela)

    elif info[1] < info[3]:
        atribui_valor_time(time_a, 0, tabela)
        atribui_valor_time(time_b, 3, tabela)
    else:
        atribui_valor_time(time_a, 1, tabela)
        atribui_valor_time(time_b, 1, tabela)

for chave in tabela.keys():
    print(f"{chave} -> {tabela[chave]}")        
    
arquivo.close()