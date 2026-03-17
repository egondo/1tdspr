produtos = [
    {"descricao": "Notebook", "quantidade": 100, "preco": 4374},
    {"descricao": "Monitor", "quantidade": 87, "preco": 750},
    {"descricao": "Placa de Video", "quantidade": 140, "preco": 3500},
    {"descricao": "SSD", "quantidade": 800, "preco": 250},
    {"descricao": "Processador", "quantidade": 340, "preco": 1780},
    {"descricao": "Impressora", "quantidade": 150, "preco": 899}
]

def venda_produto(prod: str, qtd: int, cliente: dict) -> dict:
    for item in produtos:
        if item['descricao'] == prod:
            if item['quantidade'] >= qtd:
                nota_fiscal = {
                    "numero": 2764, "produto": prod, "data_entrega": "20/03/2026",
                    "valor_total": qtd * item['preco']
                }
                item['quantidade'] = item['quantidade'] - qtd
                return nota_fiscal
            else:
                raise Exception("RNx: nao tenho qtd sufic para venda")
    raise Exception("RNxx: produto não comercializado")

#nf1 = venda_produto("memoria RAM", 10, {"nome": "FIAP", "CNPJ": "838432"})
#print(nf1)

try:
    nf2 = venda_produto("Placa de Video", 10, {"nome": "FIAP", "CNPJ": "838432"})
    print(nf2)
except Exception as erro:
    print(erro)

try:
    nf3 = venda_produto("Monitor", 1000, {"nome": "FIAP", "CNPJ": "838432"})
except Exception as erro:
    print(erro)
else:
    print(nf3)

