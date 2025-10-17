n = int(input("Digite n: "))
lista = []

i = 0
while i < n:
    num = float(input("Num: "))
    lista.append(num)
    i = i + 1
 
i = 0
j = len(lista) - 1
while i <= j:
    soma = lista[i] + lista[j]
    print(soma)
    i = i + 1
    j = j - 1
