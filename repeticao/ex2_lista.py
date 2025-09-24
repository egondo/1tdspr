soma = 0
n = int(input("Informe a qtd de alunos: "))

contador = 0

while contador < n:
    nota = float(input("Informe a nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma / n
print(f"A média vale {media}")

