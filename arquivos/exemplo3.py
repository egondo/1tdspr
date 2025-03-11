import random

times =["São Paulo", "Portuguesa", "Palmeiras", "Corinthians", "Juventus", "Nacional", "Santos", "Audax", "Red Bull", "Água Santa"]

arq_jogos = open('arquivos/jogos.txt', mode="w", encoding="utf8")

for i in range(0, len(times)):
    j = i + 1
    while j < len(times):
        g_a = random.randint(0, 7)
        g_b = random.randint(0, 7)

        #print(f"{times[i]} {g_a} X {g_b} {times[j]}")
        arq_jogos.write(f"{times[i]} {g_a} X {g_b} {times[j]}\n")

        g_a = random.randint(0, 7)
        g_b = random.randint(0, 7)
        arq_jogos.write(f"{times[j]} {g_b} X {g_a} {times[i]}\n")

        j = j + 1

arq_jogos.close()