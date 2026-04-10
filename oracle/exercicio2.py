from faker import Faker
import random


f = Faker("pt_BR")
lista = ['Prevent Sênior', 'Omint', 'SUS', 'Particular', 'Sul América', 'Bradesco Saúde', 'Care Plus', 'Unimed', 'Porto Seguro']

for _ in range(100):
    i = random.randint(0, len(lista) - 1)
    data = f.date_of_birth(minimum_age=5, maximum_age=89)
    ins = f"INSERT INTO PACIENTE(nome, convenio, nascimento) VALUES('{f.name()}', '{lista[i]}', to_date('{data}', 'YYYY-MM-DD'));"
    print(ins)