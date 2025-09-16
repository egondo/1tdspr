#Classifcar o trabalhador em 4 níveis:
# a) modesto - ganha até 2 salários mínimos
# b) ok - ganha acima de 2 e até 6 salários mínimos
# c) bom - ganha acima de 6 e até 15 salários mínimos
# d) premium - ganha acima de 15 salários mínimos


salario = float(input("Valor em R$ do salário: "))
sal_min = 1518.00
qtd_sm = salario / sal_min

if qtd_sm <= 2:
    print(f"Vc ganha {qtd_sm} SM - MODESTO!")

elif qtd_sm <= 6:
    print(f"Vc ganha {qtd_sm} SM - OK!")

elif qtd_sm <= 15:
    print(f"Vc ganha {qtd_sm} SM - BOM!")

else:
    print(f"Vc ganha {qtd_sm} SM - PREMIUM!")    
