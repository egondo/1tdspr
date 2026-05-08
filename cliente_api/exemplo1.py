import requests

cep = input("CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json"

resposta = requests.get(url)

if resposta.status_code == 200:
    endereco = resposta.json()
    print(endereco)

else:
    print("Consulta não realizada")