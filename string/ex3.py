def substitui(frase: str, letra: str) -> str:
    resp = ''
    for c in frase:
        if c == letra:
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

def substitui_letras(frase: str, letras: str) -> str:
    resp = ''
    for c in frase:
        if c in letras:
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

teste = substitui_letras("Hoje esta muito quente", 'eta')
print(teste)