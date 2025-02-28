if __name__ == "__main__":

    datafile = open("arquivos/dados.txt", mode="r")
    
    #le o conteudo inteiro do arquivo retornando as informações
    #como uma lista de String
    content = datafile.readlines()

    datafile.close()

    print(type(content))

    #for record in content:
    #    print(record)

    #outra forma para percorrermo a lista
    i = 0
    while i < len(content):
        #print(content[i])
        dados = content[i].split(";")
        #dados possui as informações de uma linha
        #do arquivo separada em uma lista
        print(dados)
        print("\n")
        i = i + 1
