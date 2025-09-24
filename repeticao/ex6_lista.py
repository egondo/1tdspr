nota = int(input("Nota do aluno: "))
maior = nota
menor = nota

contador = 1
while contador < 20:
    nota = int(input("Nota do aluno: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    contador = contador + 1

print(f"A maior nota é {maior}")
print(f"A menor nota é {menor}")

