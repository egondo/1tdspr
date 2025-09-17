salario = float(input("Salário: "))
contribuicao = 0

if salario <= 1693.72:
    contribuicao = salario * 0.08

if salario > 1693.72 and salario <= 2822.90:
    contribuicao = salario * 0.09

if salario > 2822.90 and salario <= 5645.80:
    contribuicao = salario * 0.11

if salario > 5645.80:
    contribuicao = 5645.80 * 0.11

print(f"Vou contribuir com {contribuicao:.2f} para o INSS")