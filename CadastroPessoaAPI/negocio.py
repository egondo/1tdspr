import banco
import traceback

def cadastra_pessoa(pes: dict, end: dict):
    try:
        #verifica se ja existe pessoa com o cpf e o telefone
        print(pes)
        banco.insere_pessoa(pes)
        end['id_pessoa'] = pes['id']
        print(end)
        banco.insere_endereco(end)
    except Exception as erro:
        traceback.print_exc() #imprime a msg de erro
        raise Exception("Erro no banco de dados")

