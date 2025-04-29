import banco
import traceback

def cadastra_pessoa(pes: dict):
    try:
        banco.insere_pessoa(pes)
    except Exception as e:
        traceback.print_exc()
        raise Exception("Erro no cadatramento da pessoa!")
    
def recupera_todas_pessoas():
    resp = []
    dados = banco.recupera_pessoa()
    for reg in dados:
        pes = {
            "id": reg[0],
            "nome": reg[1],
            "nascimento": reg[2],
            "altura": reg[3],
            "peso": reg[4],
            "sexo": reg[5]
        }
        resp.append(pes)

    return resp
