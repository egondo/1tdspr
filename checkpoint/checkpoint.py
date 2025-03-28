import json

def converte(campos: list) -> dict:
    prod = {
        'codigo': campos[0],
        'produto': campos[1],
        'quantidade': int(campos[2]),
        'preco': float(campos[3]),
        'local': campos[4]
    }
    return prod

def cria_dicionario_regiao() -> dict:
    dic = {
        'Curitiba': 'Sul',
        'Porto Alegre': 'Sul',
        'Florianópolis': 'Sul',
        'São Paulo': 'Sudeste',
        'Rio de Janeiro': 'Sudeste',
        'Belo Horizonte': 'Sudeste',
        'Vitória': 'Sudeste',
        'Manaus': 'Norte',
        'Belém': 'Norte',
        'Brasília': 'Centro-Oeste',
        'Campo Grande': 'Centro-Oeste',
        'Goiânia': 'Centro-Oeste',
        'Cuiabá': 'Centro-Oeste'
    }
    return dic

def buscar_regiao(local: str, dicionario: dict) -> str:
    if local in dicionario:
        return dicionario[local]
    else:
        return 'Nordeste'

#1
try:
    with open('produtos.txt', mode="r") as arq:
        lista = arq.readlines()

    #preciso remover a primeira entrada da lista 
    lista.pop(0)
    #2
    lista_produtos = []
    for reg in lista:
        campos = reg.replace("\n", '').split(';')
        #print(campos)
        dic_prod = converte(campos)
        lista_produtos.append(dic_prod)
    #print(lista)

    #3
    dic_regiao = cria_dicionario_regiao()
    for produto in lista_produtos:
        regiao = buscar_regiao(produto['local'], dic_regiao)
        produto['regiao'] = regiao
        #print(produto)

    #4
    with open('produtos.json', mode='w') as arq:
        json.dump(lista_produtos, arq, indent=4)

    print("Arquivo convertido com sucesso!")    
except Exception as erro:
    print(erro)