with open("dados.txt", mode="r") as file:
    info = file.read()

print(info)

lista = info.split("\n")
print(lista)
profs = ["Edu Gondo", "Ubirajara", "Marcel", "Rafa Desiderio", "Vinicius", "Karina"]

i = 0
while i < len(lista):
    lista[i] = f"{lista[i]}: {profs[i]}"
    i = i + 1

with open("dados_2.txt", mode="w") as file:
    for info in lista:
        file.write(info)
        file.write("\n")

print("Gravacao efetuada com sucesso")