soma = 0

num = int(input("Informe o numero: "))
while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Informe o numero: "))    

print(f"A soma dos pares vale {soma}")
