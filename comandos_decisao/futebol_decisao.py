gols_A = int(input("Gols Time A: "))
gols_B = int(input("Gols Time B: "))

if gols_A >= gols_B:
    if gols_A > gols_B:
        print("Time A venceu!")
    else:
        print("Empatou a partida")
else:
    print("Time B venceu!")
    