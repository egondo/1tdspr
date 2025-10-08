cpf = int(input("CPF: "))
aux_cpf = cpf #guardando o cpf para o segundo digito
soma = 0
mult = 2

while cpf != 0:
    dig = cpf % 10
    cpf = cpf // 10
    soma = soma + mult * dig
    mult = mult + 1

resto = soma % 11
if resto < 2:
    dc = 0
else:
    dc = 11 - resto

print(f"1 DC vale {dc}")
cpf = aux_cpf * 10 + dc

soma = 0
mult = 2

while cpf != 0:
    dig = cpf % 10
    cpf = cpf // 10
    soma = soma + mult * dig
    mult = mult + 1

resto = soma % 11
if resto < 2:
    dc2 = 0
else:
    dc2 = 11 - resto

print(f"Digitos de controle: {dc}{dc2}")