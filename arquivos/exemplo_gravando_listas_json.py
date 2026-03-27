import json

#Gravar o resultado da Partida entre Brasil e França

partidas = [
    {
        "casa": "Brasil",
        "visitante": "França",
        "local": "Boston",
        "gols_casa": 1,
        "gols_visitante": 2
    },
    {
        "casa": "Portugal",
        "visitante": "Polônia",
        "local": "Lisboa",
        "gols_casa": 0,
        "gols_visitante": 0
    },
        {
        "casa": "Argentina",
        "visitante": "USA",
        "local": "Buenos Aires",
        "gols_casa": 2,
        "gols_visitante": 2
    }
]

with open("lista_partidas.json", mode="w") as arq:
    json.dump(partidas, arq, indent=4)