import random

def gera_valor() -> float:
    valor = random.randint(1000_00, 10000_00)
    return valor * 0.01

produtos = ["geladeira", "celular", "smart tv", "notebook", "lavadora", "ar condicionado"]
marcas = ["Samsung", "LG", "Acer", "HP", "Midea", "Hitachi", "Motorola"]
lojas = ["Cidade São Paulo", "Eldorado", "Paulista"]

with open("faturamento_2025.txt", mode="w", encoding="utf-8") as arq:
    arq.write("produto;marca;loja;data;qtd;valor\n")
    for mes in range(1, 12):
        for dia in range(1, 30):
            for qtd in range(20):
                i = random.randint(0, len(produtos)-1)
                j = random.randint(0, len(marcas) - 1)
                k = random.randint(0, 2) #loja
                qtd = random.randint(1, 50)
                vl = gera_valor()
                if mes == 2 and dia > 28:
                    print("Data invalida!")
                else:
                    arq.write(f"{produtos[i]};{marcas[j]};{lojas[k]};")
                    arq.write(f"2025-{mes}-{dia};{qtd};{vl:.2f}\n")

