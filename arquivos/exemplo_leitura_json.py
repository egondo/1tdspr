import json

with open("lista_partidas.json", mode="r") as arq:
    lista = json.load(arq)

for item in lista:
    #print(item)
    print(f"{item['casa']} {item['gols_casa']} X {item['gols_visitante']} {item['visitante']}")