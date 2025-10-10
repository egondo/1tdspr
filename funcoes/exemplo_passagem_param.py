def contagem_regressiva(num):
    while num > 0:
        num = num - 1
    
    return num

a = 100
resp = contagem_regressiva(a)
print(f"{resp} {a}")