import banco
import traceback

def recupera_perguntas(enquete: int) -> list:
    try:
        dados = banco.recupera_perguntas_enquete(enquete)
        #converter os dados do banco para a lista de dicionarios desenhada
        retorno = []
        aux_id = -1
        info = None
        for reg in dados:
            if aux_id != reg[0]:
                aux_id = reg[0]
                info = {"id": reg[0], "numero": reg[1], "questao": reg[2], "tipo": reg[3], "itens": []}
                retorno.append(info)

            info['itens'].append(reg[4])

        return retorno
    except Exception as erro:
        traceback.print_exc()
        raise erro
    
if __name__ == "__main__":
    dados = recupera_perguntas(1)
    for reg in dados:
        print(reg)

