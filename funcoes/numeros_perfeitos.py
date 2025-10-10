def perfeito(n):
    div = 1
    soma = 0
    while div < n:
        if n % div == 0:
            soma = soma + div
        div = div + 1
    
    return soma == n

num = 1
while num < 80000:
    resp = perfeito(num)
    if resp == True:
        print(f"{num}")
    num = num + 1