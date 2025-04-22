paises = ['Brasil', 'Irã', 'Cuba', 'China']

for pais in paises:
    if pais == 'Cuba':
        #alterar o pais para Chipre
        #paises[?] = 'Chipre'
        pais = 'Chipre'
    print(pais)

paises.insert(0, '')

for i, pais in enumerate(paises):
    print(i, pais)

for i in range(len(paises)):
    if paises[i] == 'Cuba':
        paises[i] = 'Chipre'    

print(paises)
