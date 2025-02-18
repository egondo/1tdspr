import palavras_forca as pf

def gera_segredo(word: str, letras: str) -> str:
    resp = ''
    for c in word:
        if c.lower() in letras:
            resp = resp + c + ' '
        else:
            resp = resp + '_ '
    return resp


print("Bem vindo ao jogo da forca 1tdspr")
palavra = pf.get_country()
erros = 0
letras_chutadas = ' '
segredo = gera_segredo(palavra, letras_chutadas)

while erros < 6 and '_' in segredo:
    print(segredo)
    print(f'Erros: {erros}')
    letra = input("Letra: ")
    letras_chutadas = letras_chutadas + letra
    if not letra in palavra:
        erros = erros + 1
    segredo = gera_segredo(palavra, letras_chutadas)

if erros >= 6:
    print(f'Você perdeu, a palavra era {palavra}')
else:
    print(f'Parabéns, a palavra era {palavra}')






