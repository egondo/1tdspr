def is_prime(num: int) -> bool:
    if num == 1:
        return False
    div = 2
    while num % div != 0:
        div = div + 1
    
    if div == num:
        return True
    else:
        return False
    

candidato = 1
contador = 0
resp = ""
while contador < 100_000:
    if is_prime(candidato):
        #print(candidato)
        resp = f"{resp}, {candidato}"
        contador = contador + 1    
    candidato = candidato + 1

print(resp)
