#entrada de dados
#temp = input("Numero: ")
#num = int(temp)

num = int(input("Numero: "))
resto = num % 2

#verificacao, olhar qual valor esta armazenado em resto
if resto == 0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")
    
