if __name__ == "__main__":

    with open("arquivos/curriculo.html", mode="r") as arq:
        conteudo = arq.read()

    print(type(conteudo))
    print(conteudo)

