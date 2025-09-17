salario = float(input("Salário: "))
contribuicao = 0

if salario <= 1693.72:
    contribuicao = salario * 0.08
elif salario <= 2822.90:
    contribuicao = salario * 0.09
elif salario <= 5645.80:
    contribuicao = salario * 0.11
else:
    contribuicao = 5645.80 * 0.11

print(f"Vou contribuir com {contribuicao:.2f} para o INSS")
