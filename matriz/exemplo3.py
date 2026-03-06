def calcula_media(notas: list) -> float:
    qtd = len(notas)
    soma = 0 
    for nt in notas:
        soma = soma + nt

    return soma / qtd


notas = [
    [6.8, 4.2, 5.9, 8.1, 7.8],
    [4.7, 6.8, 7.5, 8.5, 2.8],
    [4.5, 8.7, 7.1, 6.5, 8.0]
]

for aluno in notas:
    media = calcula_media(aluno)
    print(f"A media foi {media}")