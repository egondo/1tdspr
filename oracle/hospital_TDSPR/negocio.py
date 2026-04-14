import banco

#funcionalidade de pegar a senha no totem
def pega_senha_totem(nome: str, cpf: str) -> int:
    pac = banco.recupera_paciente_cpf(cpf)

    if pac: #paciente ja existe na base
        #inserir o atendimento com os dados do paciente
        at = {"chegada": '10-04-2026 10:34', 'saida': None, 'desfecho': 'em atendimento', 'pac_id': pac[0]}
        banco.insere_atendimento(at)
    

if __name__ == "__main__":
    pega_senha_totem('Milena Brito', '64')
