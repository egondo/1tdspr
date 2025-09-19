#Faça uma execucao no papel deste algoritmo

soma = 0
num = int(input("Num: "))

while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Num: "))

print(soma)
