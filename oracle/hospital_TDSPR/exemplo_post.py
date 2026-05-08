import requests

#:peso, :altura, :pressao, :batimento, :temperatura, :sintomas, :atend_id_fk, :func_id_fk

peso = float(input("Peso: "))
altura = float(input("Altura: "))
pressao = input("Pressao: ")
batimento = int(input("Batimento: "))
temperatura = float(input("Temp: "))
sintomas = input("Sintomas: ")

triagem = {
    "peso": peso, "altura": altura, "pressao": pressao, 
    "batimento": batimento, "temperatura": temperatura,
    "sintomas": sintomas, "func_id_fk": 1
}

url = f"https://tdspr.onrender.com/hospital/triagem/66"

resp = requests.post(url, json=triagem)
if resp.status_code == 200:
    print("Triagem cadastrada com sucesso!")
    print(resp.json())
else:
    print("Erro no cadastro da triagem!")