arq = open("dados_2.txt", mode="a")
lista = ["Nano Courses: Luis Carlos Silva\n", 
         "Shift: Thiago Yamamoto\n"]

arq.writelines(lista)
arq.close()

