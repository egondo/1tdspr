frase = 'Socorram-me, subi no ônibus em Marrocos'

i = 0
while i < len(frase):
    print(frase[i])
    i = i + 1

texto = ""
for letra in frase:
    texto = letra + texto

print(texto)