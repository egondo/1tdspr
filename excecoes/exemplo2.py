try:
    numero = float(input("Numero: "))
    divisor = float(input("Divisor: "))
    resultado = numero / divisor
except ZeroDivisionError as erro1:
    print("Deu erro pq vc tentou dividir por 0")
except ValueError as erro2:
    print("Vc tentou converter uma string invalida para numero")
else:
    print(resultado)


