matriz = []

for i in range(4):
    matriz.append([0] * 5)

#matriz[0][0] = 1
#matriz[0][1] = 2
#matriz[0][2] = 3
#matriz[0][3] = 4
#matriz[0][4] = 5

num = 1

for i in range(4):
    j = 0
    while j < 5:
        matriz[i][j] = num
        j = j + 1
        num = num + 1


for lin in matriz:
    print(lin)


