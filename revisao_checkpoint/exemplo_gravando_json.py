import json

dados = [
    {
        "valor": "As",
        "naipe": "paus"
    },
    {
        "valor": "7",
        "naipe": "copas"
    },
    {
        "valor": "4",
        "naipe": "ouros"
    }
]

arq = open("cartas.txt", mode="w")

c = {"valor": "K", "naipe": "espadas"}
dados.append(c)

json.dump(dados, arq)
arq.close()
