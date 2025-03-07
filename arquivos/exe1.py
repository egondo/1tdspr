import random

def amanha(dia: int, mes: int) -> list:
    #retorna uma lista com 2 posicoes, na posicao 0 temos o novo dia e na posição o mês do novo dia
    if dia < 28:
        return [dia + 1, mes]
    else:
        if mes < 12:
            return [1, mes + 1]
        else:
            return [10, 10]

if __name__ == "__main__":
    data = [1, 1]
    prod = ["geladeira", "TV", "notebook", "lava-roupa", "celular", "pipoqueira"]

    marca = ["samsung", "LG", "Asus", "Acer", "Brastemp", "Xiaomi", "Panasonic", "Arno"]

    loja = ["Plaza Sul", "Center Norte", "Light"]
    
    arq = open("/Users/eduardogondo/faturamento.txt", mode="w")

    i = 0
    while i < 5000:
        data = amanha(data[0], data[1])
        for j in range(9):
            pos = random.randint(0, len(prod) - 1)
            p = prod[pos]
            pos = random.randint(0, len(marca) - 1)
            m = marca[pos]
            qtd = random.randint(5, 100)
            prc = random.random() * 4000

            for lj in loja:
                linha = f"{p};{m};{lj};{data[0]}/{data[1]}/2022;{qtd};{prc}"
                #print(linha)
                arq.write(linha + "\n")

        i = i + 20

    arq.close()