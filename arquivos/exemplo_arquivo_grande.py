import datetime

with open('dieese.dump', mode="r", encoding="ISO8859-1") as arq:
    ini = datetime.datetime.now()
    lin = 0
    for info in arq:
        lin = lin + 1

    fim = datetime.datetime.now()

print(f"Tempo de leitura: {fim - ini}")
print(f"Linhas {lin}")