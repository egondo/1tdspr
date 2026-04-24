import banco
import util

#funcionalidade de pegar a senha no totem
def pega_senha_totem(nome: str, cpf: str) -> int:
    pac = banco.recupera_paciente_cpf(cpf)
    senha = banco.recupera_senha()
    chegada = util.get_data_atual()

    if pac == None:
        pac = {"nome": nome, "cpf": cpf, "convenio": None, "nascimento": None}
        banco.insere_paciente(pac)
        at = {"chegada": chegada, 'saida': None, 'desfecho': 'em atendimento', 'pac_id': pac['id'], "senha": senha}
    else:
        at = {"chegada": chegada, 'saida': None, 'desfecho': 'em atendimento', 'pac_id': pac[0], "senha": senha}
    banco.insere_atendimento(at)

    return senha
    

def grava_triagem(triagem: dict, senha: int):
    data = util.get_data_atual()
    atend = banco.recupera_atendimento_senha(senha)
    triagem['atend_id_fk'] = atend['atend_id']
    triagem['data'] = data
    banco.insere_triagem(triagem)

def rec_paciente_senha(senha: int) -> dict:
    pac = banco.recupera_paciente_senha(senha)
    return pac

def grava_prontuario(pront: dict, senha: int):
    atd = banco.recupera_atendimento_senha(senha)
    pront['atend_id_fk'] = atd['atend_id']
    pront['data'] = util.get_data_atual()
    banco.insere_prontuario(pront)

def atualiza_paciente_recepcao(paciente: dict):
    banco.atualiza_paciente(paciente)
    

if __name__ == "__main__":
    #senha = pega_senha_totem('Isa Nunes', '55566677788')
    #print(senha)

    #senha = pega_senha_totem('Andreia Souza', '3')
    #print(senha)
    triagem = {"pressao": "12/8", "batimento": 125, "temperatura": 39, "altura": 1.75, "peso": 68, 'func_id_fk': 1, "sintomas": "vertigem, dor de cabeça, indisposição"}

    grava_triagem(triagem, 18)
