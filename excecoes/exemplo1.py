produtos = [
    {"descricao": "Notebook", "quantidade": 100, "preco": 4374},
    {"descricao": "Monitor", "quantidade": 87, "preco": 750},
    {"descricao": "Placa de Video", "quantidade": 140, "preco": 3500},
    {"descricao": "SSD", "quantidade": 800, "preco": 250},
    {"descricao": "Processador", "quantidade": 340, "preco": 1780},
    {"descricao": "Impressora", "quantidade": 150, "preco": 899}
]

try:
    print(produtos[1])
    print(produtos[0]['preço'])
except Exception as erro:
    print("Ocorreu um erro! Contate o adm do sistema!")
    print(erro)

print("Finalizando o programa")