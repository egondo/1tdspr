num_a = float(input("1 número: "))
op = input("Operador (+-/*): ")
num_b = float(input("2 número: "))

resultado = 0
fez_conta = True

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '/':
    resultado = num_a / num_b
elif op == '*':
    resultado = num_a * num_b
else:
    print("Operador inválido!")
    fez_conta = False
    #quit() #encerra o programa

if fez_conta == True:
    print(f"{num_a} {op} {num_b} = {resultado}")