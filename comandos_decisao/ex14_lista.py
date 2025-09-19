dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data inválida")
    quit() #fecha o programa quando executa a instrucao


if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False

if mes == 2:
    if dia > 28:
        if dia == 29 and bissexto:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        print("Data válida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia == 31:
        print("Data inválida")
    else:
        print("Data válida")
else:
    print("Data válida")