def mmc(a, b):
    multiplo = a
    while multiplo % a != 0 or multiplo % b != 0:
        multiplo = multiplo + 1
    return multiplo


x = 8
y = 14
resp = mmc(x, y)
print(resp)
