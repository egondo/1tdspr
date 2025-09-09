temp = input("Informe o RM: ")
rm = int(temp)

acumulador = 0

#1 digito
dig = rm % 10
acumulador = acumulador + dig
rm = rm // 10

#2 digito
dig = rm % 10
acumulador = acumulador + dig
rm = rm // 10

#3 digito
dig = rm % 10
acumulador = acumulador + dig
rm = rm // 10

#4 digito
dig = rm % 10
acumulador = acumulador + dig
rm = rm // 10

#5 digito
dig = rm % 10
acumulador = acumulador + dig
rm = rm // 10

print("A soma dos digito vale", acumulador)
print(f"A soma dos digitos vale {acumulador}")