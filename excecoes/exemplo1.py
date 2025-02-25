if __name__ == "__main__":

    nome = input("Digite o nome: ")
    mes_nasc = int(input("Digite o mês de nascimento: "))

    num_a = float(input("Digite número A: "))
    num_b = float(input("Digite número B: "))
    quociente = num_a / num_b
    print(f"{num_a} / {num_b} = {quociente}")

    times = ["Corinthians", "Santos", "Palmeiras"]
    i = 0
    print(times[i])

    arq = open("excecoes/exemplo1.py", mode="r")
    conteudo = arq.read()
    print(conteudo)
    arq.close()

