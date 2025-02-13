def substitui(frase: str, letra: str) -> str:
    resp = ''
    for c in frase:
        if c == letra:
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

teste = substitui("Hoje esta muito quente", 'e')
print(teste)