agenda = {'ana': 'ana@gmail.com', 'beto': 'beto@yahoo.com', 'cida': 'cida@zip.com.br'}
print("")
print(agenda)
print("")

agenda['dani'] = "daniel@fiap.com.br"

print(agenda)
print("")
agenda['beto'] = 'robertosoares@gmail.com'
print(agenda)

#endereco = agenda['edu'] nao existe chave edu no dicionario
#print(endereco)

for chave in agenda.keys():
    print(f"{chave} => {agenda[chave]}")

    
