import os
import random

def tracejado(palavra: str, lista: list) -> str:
    resp = ""
    i = 0
    while i < len(palavra):
        if lista[i]:
            resp = resp + palavra[i] + " "
        else:
            resp = resp + "_ "
        i = i + 1
    return resp

def enforcou(erros: int) -> bool:
    return erros >= 6

def busca(palavra: str, letra: str, lista: list) -> bool:
    i = 0
    encontrou = False
    while i < len(palavra):
        if palavra[i] == letra:
            lista[i] = True
            encontrou = True
        i = i + 1
    return encontrou

def acertou(lista: list) -> bool:
    if False in lista:
        return False
    else:
        return True    

def imprime(palavra, lista, erros):
    if os.name == "NT":
        os.system("cls")
    else:
        os.system("clear")
    print("HANGMAN")
    print(tracejado(palavra, lista))
    print(f"Erros: {erros}")
    
def sorteio() -> str:
    lista = ["melancia", "morango", "maracuja", "abacaxi", "tamarindo", "jabuticaba", "jatoba", "tangerina", "mexerica"]
    n = random.randint(0, len(lista) - 1)
    return lista[n]

segredo = sorteio()
erros = 0
#criando uma lista de booleanos para controlar quando
#a letra deve ser exibida
descobriu = [False] * len(segredo)

while not enforcou(erros) and not acertou(descobriu): 
    imprime(segredo, descobriu, erros)
    letra = input("Letra: ")
    if not busca(segredo, letra, descobriu):
        erros = erros + 1

if enforcou(erros):
    print(f"Você perdeu, a palavra era {segredo}")
else:
    print(f"Você ganhou, a palavra era {segredo}")