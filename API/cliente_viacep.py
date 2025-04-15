import requests

cep = "04137-000"

link = f"https://viacep.com.br/ws/{cep}/json"
objeto = requests.get(link)
print(type(objeto))
info = objeto.json()
print(info)


url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json"
objeto = requests.get(url)
dado = objeto.json()
print(dado)

url = "https://dragonball-api.com/api/characters"
objeto = requests.get(url)
dado = objeto.json()
print(dado)