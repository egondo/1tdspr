def aumento(valor, percentual):
    novo_valor = (1 + percentual / 100) * valor
    #print(novo_valor)
    return novo_valor




resposta = aumento(350, 15)
#aqui poderiamos pegar a resposta e mostrar:
#a) página html
#b) dispositivo mobile
#c) componente gráfico de janelas (window) (GUI)
#d) terminal
print(resposta)
