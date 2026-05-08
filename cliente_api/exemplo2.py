import requests

cpf = input("CPF: ")
nome = input("Nome: ")
url = f"https://tdspr.onrender.com/hospital/senha/{cpf}/{nome}"

resposta = requests.get(url)

if resposta.status_code == 200:
    senha = resposta.json()
    print(senha)

else:
    print("Geraçao de senha com problemas")