num = int(input("Informe o numero decimal: "))
soma = 0
pot_dez = 1

while num != 0:
    resto = num % 2
    num = num // 2
    soma = soma + pot_dez * resto
    pot_dez = pot_dez * 10

print(f"Binario: {soma}")




#resto = num % 2
#num = num // 2

#resto = num % 2
#num = num // 2