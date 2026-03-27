import json

#Gravar o resultado da Partida entre Brasil e França

partida = {
    "casa": "Brasil",
    "visitante": "França",
    "local": "Boston",
    "gols_casa": 1,
    "gols_visitante": 2
}

with open("partida.json", mode="w") as arq:
    json.dump(partida, arq, indent=4)