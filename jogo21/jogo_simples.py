import baralho as bar

deck = bar.cria()

bar.embaralha(deck)
c1 = bar.compra(deck)
c2 = bar.compra(deck)

if c1[0] > c2[0]:
    print(f"jogador 1 ganhou {bar.to_string(c1)} {bar.to_string(c2)}")
else:
    print(f"jogador 2 ganhou {bar.to_string(c2)} {bar.to_string(c1)}")